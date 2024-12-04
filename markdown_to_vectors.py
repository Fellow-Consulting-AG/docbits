import os
import glob
from typing import List, Tuple
import markdown
from bs4 import BeautifulSoup
import openai
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import numpy as np
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Database configuration
DB_CONNECTION = os.getenv('DATABASE_URL', 'postgresql://localhost/vector_db')

def init_database():
    """Initialize the database with required extensions and tables."""
    engine = create_engine(DB_CONNECTION)
    
    with engine.connect() as conn:
        # Create pgvector extension if it doesn't exist
        conn.execute(text('CREATE EXTENSION IF NOT EXISTS vector;'))
        
        # Create documents table
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS documents (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                content TEXT NOT NULL,
                url TEXT,
                embedding vector(1536),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        '''))
        
        conn.commit()

def get_embedding(text: str) -> List[float]:
    """Get OpenAI embedding for the given text."""
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

def process_markdown(file_path: str) -> Tuple[str, str]:
    """Process markdown file and return filename and clean text content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert markdown to HTML
    html = markdown.markdown(content)
    
    # Extract text from HTML
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    
    return os.path.basename(file_path), text

def chunk_text(text: str, max_tokens: int = 8000) -> List[str]:
    """Split text into chunks that fit within token limits."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        # Rough estimate: 1 word ≈ 1.3 tokens
        word_tokens = len(word) * 1.3
        if current_length + word_tokens > max_tokens:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = word_tokens
        else:
            current_chunk.append(word)
            current_length += word_tokens
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def main():
    # Initialize database
    init_database()
    engine = create_engine(DB_CONNECTION)
    
    # Find all markdown files
    markdown_files = glob.glob('**/*.md', recursive=True)
    
    for file_path in markdown_files:
        try:
            filename, content = process_markdown(file_path)
            chunks = chunk_text(content)
            
            # Generate URL for the document
            repo_url = "https://github.com/docbits/docbits/blob/main/"
            relative_path = os.path.relpath(file_path)
            doc_url = repo_url + relative_path
            
            for i, chunk in enumerate(chunks):
                embedding = get_embedding(chunk)
                
                # Store in database
                with engine.connect() as conn:
                    conn.execute(
                        text('''
                            INSERT INTO documents (filename, content, url, embedding)
                            VALUES (:filename, :content, :url, :embedding::vector)
                        '''),
                        {
                            'filename': f"{filename}_chunk_{i}",
                            'content': chunk,
                            'url': doc_url,
                            'embedding': embedding
                        }
                    )
                    conn.commit()
            
            print(f"Processed: {filename}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

if __name__ == "__main__":
    main()

#!/bin/bash

# Find all markdown files in the current directory and subdirectories
find readme -name "*.md" | while read -r file; do
  # Define output PDF file name
  output_file="${file%.md}.pdf"

  # Extract the base name of the file for the title
  base_name=$(basename "$file" .md)
  
  # Convert Markdown to PDF with title metadata
  pandoc "$file" -o "$output_file" --pdf-engine=wkhtmltopdf --metadata=title="$base_name"
  
  # Print status message
  echo "Converted $file to $output_file"
done


import os
import re

def is_bad_filename(filename):
    """
    Checks if the filename contains spaces or parentheses.
    """
    if ' ' in filename or '(' in filename or ')' in filename:
        return True
    if '%20' in filename:
        return True
    return False

def check_images(root_dir):
    # Regex for Markdown images: ![alt](src)
    # We want to match ! [ ... ] ( ... )
    img_regex_md = re.compile(r'!\[(.*?)\]\((.*?)\)')
    
    # Regex for HTML img tags
    img_tag_regex = re.compile(r'<img\s+[^>]*?>', re.IGNORECASE)
    
    issues = []

    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules' and d != 'venv']

        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    continue

                for i, line in enumerate(lines):
                    # Check Markdown images
                    for match in img_regex_md.finditer(line):
                        alt_text = match.group(1)
                        full_src = match.group(2)
                        
                        # Extract the probable filename for checking
                        # If src has a title part like "url 'title'", split it.
                        # We'll just take the first part split by space if the second part starts with " or '
                        parts = full_src.split(' ', 1)
                        src_check = parts[0]
                        # If there's a title, we ignore it for filename check, 
                        # BUT if the space was part of the filename (bad!), we might have split it.
                        # However, since we flag bad filenames (spaces), splitting by space effectively catches "contains space" 
                        # because `full_src` had a space.
                        # Wait, if full_src is "my image.png", split gives "my".
                        # `is_bad_filename("my")` is False.
                        # So we should check `full_src` for bad chars BEFORE splitting?
                        # No, `full_src` is everything inside (). 
                        # If it is "my image.png", then it has a space.
                        # If it is "image.png 'Title'", it has a space.
                        # Markdown allows title.
                        # If `full_src` has a space, it *might* be a title separator, OR a bad filename.
                        # If it looks like a title (starts with quote), then the space was a separator.
                        # If the part after space doesn't look like a title, then the space is likely in the filename.
                        
                        # Let's simple check:
                        # If space in full_src:
                        #   Check if it matches pattern `url "title"` or `url 'title'`.
                        #   If so, the url is the part before space.
                        #   Else, the url is full_src (and it has a space -> bad).
                        
                        src_final = full_src
                        if ' ' in full_src:
                            # Check for title pattern
                            m_title = re.match(r'^(.*?)(\s+["\'].*["\\])$', full_src)
                            if m_title:
                                src_final = m_title.group(1)
                            else:
                                src_final = full_src # Contains space, so it's the filename with space

                        bad_name = is_bad_filename(src_final)
                        missing_alt = not alt_text.strip()
                        
                        if bad_name or missing_alt:
                            issues.append({
                                'file': filepath,
                                'line': i + 1,
                                'type': 'markdown',
                                'src': src_final,
                                'alt': alt_text,
                                'bad_filename': bad_name,
                                'missing_alt': missing_alt
                            })

                    # Check HTML images
                    for match in img_tag_regex.finditer(line):
                        tag = match.group(0)
                        
                        src_match = re.search(r'src=["\'](.*?)["\']', tag, re.IGNORECASE)
                        src = src_match.group(1) if src_match else ""
                        
                        alt_match = re.search(r'alt=["\'](.*?)["\']', tag, re.IGNORECASE)
                        alt_text = alt_match.group(1) if alt_match else ""
                        
                        bad_name = is_bad_filename(src)
                        missing_alt = not alt_text.strip()
                        
                        if bad_name or missing_alt:
                            issues.append({
                                'file': filepath,
                                'line': i + 1,
                                'type': 'html',
                                'src': src,
                                'alt': alt_text,
                                'bad_filename': bad_name,
                                'missing_alt': missing_alt
                            })

    return issues

if __name__ == "__main__":
    current_dir = os.getcwd()
    results = check_images(current_dir)
    results.sort(key=lambda x: x['file'])
    
    print(f"Found {len(results)} image references with issues (Bad Filename OR Missing Alt).\n")
    
    header = f"{ 'File Path':<60} | {'Line':<5} | {'Issues':<25} | {'Image Source'}"
    print(header)
    print("-" * len(header))
    
    for item in results:
        issue_desc = []
        if item['bad_filename']: issue_desc.append("Bad Filename")
        if item['missing_alt']: issue_desc.append("Missing Alt")
        
        rel_path = os.path.relpath(item['file'], current_dir)
        display_path = rel_path
        if len(display_path) > 58:
            display_path = "..." + display_path[-55:]
            
        print(f"{display_path:<60} | {item['line']:<5} | {', '.join(issue_desc):<25} | {item['src']}")
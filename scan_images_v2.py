import os
import re
import json

def is_bad_filename(filename):
    return ' ' in filename or '(' in filename or ')' in filename

def get_context(filepath, image_filename):
    context = ""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if image_filename in line:
                    start = max(0, i - 2)
                    end = min(len(lines), i + 3)
                    context += "".join(lines[start:end])
                    break
    except:
        pass
    return context.strip()

def find_usages(filename, root_dir):
    usages = []
    # Regex to match filename ensuring it's a distinct file reference
    # Matches /filename" or /filename) or (filename) or "filename"
    # Escaping regex characters in filename (like parenthesis)
    escaped_filename = re.escape(filename)
    pattern = re.compile(r'([/(])' + escaped_filename + r'([)"\'])')
    
    for root, _, files in os.walk(root_dir):
        if '/.' in root or '\\.' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if pattern.search(content):
                            usages.append(path)
                except:
                    pass
    return usages

def scan_assets(asset_dirs, limit=10):
    bad_images = []
    scanned_files = set()
    
    for asset_dir in asset_dirs:
        if not os.path.exists(asset_dir):
            continue
        
        files = sorted(os.listdir(asset_dir))
        
        for filename in files:
            if filename in scanned_files:
                continue
            scanned_files.add(filename)
            
            if is_bad_filename(filename):
                full_path = os.path.join(asset_dir, filename)
                usages = find_usages(filename, '.')
                
                if usages:
                    context_snippets = {}
                    for usage in usages:
                        context_snippets[usage] = get_context(usage, filename)
                        
                    bad_images.append({
                        'original_path': full_path,
                        'filename': filename,
                        'usages': usages,
                        'contexts': context_snippets
                    })
                    
                    if len(bad_images) >= limit:
                        return bad_images
    return bad_images

if __name__ == "__main__":
    dirs = ['.gitbook/assets', 'readme/.gitbook/assets']
    results = scan_assets(dirs, limit=10)
    print(json.dumps(results, indent=2, ensure_ascii=False))

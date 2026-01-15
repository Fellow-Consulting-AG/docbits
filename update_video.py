import os
import subprocess

branches = ["fr", "de", "es", "it", "pl", "pt", "nl"]
video_embed = '
{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}
'

def update_files_in_branch(branch):
    print(f"Updating branch: {branch}")
    subprocess.run(["git", "checkout", branch], check=True)
    
    # Find files related to Power BI in advanced-functions-and-tools
    result = subprocess.run(
        ["git", "grep", "-l", "Power BI", "--", "readme/advanced-functions-and-tools/**"],
        capture_output=True, text=True
    )
    files = result.stdout.strip().split('\n')
    
    modified = False
    for file_path in files:
        if not file_path or not os.path.exists(file_path):
            continue
            
        print(f"  Processing {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        inserted = False
        file_modified = False
        for i, line in enumerate(lines):
            new_lines.append(line)
            # Insert after the first paragraph (first non-empty line after headers)
            # Avoid inserting into sub-pages that are just lists of links or tables if possible
            # But the requirement was "overview page AND two sub-pages"
            if not inserted and line.strip() and not line.startswith('#') and not line.startswith('---'):
                # Check if it's already there
                if any('youtu.be/O1MtuXf_R_M' in l for l in lines):
                    inserted = True
                    continue
                new_lines.append(video_embed)
                inserted = True
                file_modified = True
        
        if file_modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            modified = True
    
    if modified:
        # Commit changes
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "docs: embed Power BI integration video"], check=True)

try:
    for branch in branches:
        update_files_in_branch(branch)
    
    # Back to main
    subprocess.run(["git", "checkout", "main"], check=True)
    print("All branches updated successfully.")
except Exception as e:
    print(f"Error: {e}")
    subprocess.run(["git", "checkout", "main"], check=True)
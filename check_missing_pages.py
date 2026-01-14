import subprocess
import sys

def get_files_from_branch(branch):
    """Get a set of .md files in the readme/ directory for a given branch."""
    try:
        # git ls-tree -r --name-only <branch> readme/
        result = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", branch, "readme/"],
            capture_output=True, text=True, check=True
        )
        files = set(f for f in result.stdout.splitlines() if f.endswith('.md'))
        return files
    except subprocess.CalledProcessError:
        print(f"Warning: Could not get file list for branch '{branch}'. It might not exist.")
        return set()

def main():
    source_branch = "main"
    languages = ["de", "es", "fr", "it", "pl", "pt", "nl", "tr"]
    
    print(f"Fetching file list from source branch: {source_branch}...")
    source_files = get_files_from_branch(source_branch)
    print(f"Total documentation pages in '{source_branch}': {len(source_files)}\n")

    for lang in languages:
        print(f"--- Checking language: {lang} ---")
        lang_files = get_files_from_branch(lang)
        
        if not lang_files:
            print(f"  No files found or branch missing.\n")
            continue

        missing_files = sorted(list(source_files - lang_files))
        count = len(missing_files)
        
        print(f"  Pages present: {len(lang_files)}")
        print(f"  Missing pages: {count}")
        
        if count > 0:
            print(f"  Missing files list (top 10):")
            for f in missing_files[:10]:
                print(f"    - {f}")
            if count > 10:
                print(f"    ... and {count - 10} more.")
        else:
            print("  All pages translated (or at least present).")
        print("")

if __name__ == "__main__":
    main()

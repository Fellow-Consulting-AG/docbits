import subprocess
import sys

def get_files_from_branch(branch):
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", branch, "readme/"],
            capture_output=True, text=True, check=True
        )
        files = set(f for f in result.stdout.splitlines() if f.endswith('.md'))
        return files
    except subprocess.CalledProcessError:
        return set()

def main():
    source_branch = "main"
    languages = ["de", "es", "fr", "it", "pl", "pt", "nl", "tr"]
    source_files = get_files_from_branch(source_branch)
    for lang in languages:
        print(f"--- {lang} ---")
        lang_files = get_files_from_branch(lang)
        missing_files = sorted(list(source_files - lang_files))
<<<<<<< Updated upstream
        for f in missing_files[:100]:
=======
        for f in missing_files[:10]:
>>>>>>> Stashed changes
            print(f)
        print("")

if __name__ == "__main__":
    main()

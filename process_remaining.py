import os
import subprocess

BRANCHES = ["tr", "fr", "it", "pl", "pt", "nl"]

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e.stderr}")
        return False
    return True

def process_branch(branch):
    print(f"=== Processing branch: {branch} ===")
    
    # Clean working directory but EXCLUDE our scripts and json
    # git clean -fd -e filename -e filename
    # Git clean might not support -e in older versions, but likely yes.
    # Note: filenames must be relative to root.
    clean_cmd = "git clean -fd -e filename_mapping.json -e multi_lang_fix.py -e process_remaining.py"
    
    # First reset modified files
    run_command("git checkout .")
    
    # Then clean untracked files
    run_command(clean_cmd)

    # Checkout
    if not run_command(f"git checkout {branch}"):
        print(f"Failed to checkout {branch}. Skipping.")
        return

    # Run Fix
    if not run_command("python3 multi_lang_fix.py"):
        print(f"Failed to run fix on {branch}.")
        return

    # Git Add
    if not run_command("git add ."):
        return

    # Git Commit
    status = subprocess.run("git status --porcelain", shell=True, text=True, stdout=subprocess.PIPE).stdout
    if not status.strip():
        print(f"No changes to commit on {branch}.")
    else:
        if not run_command(f'git commit -m "chore(assets): rename bad filenames and update references with {branch} alt text"'):
            return
        
        # Git Push
        if not run_command(f"git push origin {branch}"):
            print(f"Failed to push {branch}.")

def main():
    for branch in BRANCHES:
        process_branch(branch)

if __name__ == "__main__":
    main()

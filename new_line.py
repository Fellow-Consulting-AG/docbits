import os
import sys

def add_newline_to_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                with open(file_path, 'a') as file:
                    file.write('\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_newline.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        if os.path.isdir(directory_path):
            add_newline_to_files(directory_path)
        else:
            print(f"The provided path '{directory_path}' is not a valid directory.")

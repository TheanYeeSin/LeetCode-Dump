import os
import sys


def generate_files(id: int, name: str):

    # CREATE PYTHON FOLDER IF NOT EXIST
    if not os.path.exists("Python"):
        os.makedirs("Python")

    # CREATE NEW LEETCODE FOLDER IF NOT EXIST
    folder_path = os.path.join("Python", f"[{id}]{name}")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # CREATE PYTHON FILE
    python_file = os.path.join(folder_path, f"[{id}]{name}.py")
    with open(python_file, "w") as file:
        file.write("# Your Python code goes here.")

    # CREATE README.MD FILE
    readme_file = os.path.join(folder_path, "README.md")
    readme_content = f"""
# {name}

Difficulty: [EDIT HERE]

# Question Description

[EDIT HERE]

# Solution

[{name}]([{id}]{name}.py)
    
    """
    with open(readme_file, "w") as file:
        file.write(readme_content)

    print(f"Files '{python_file}' and '{readme_file}' generated successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_leetcode_folder.py <id> <name>")
        sys.exit(1)

    id = sys.argv[1]
    name = sys.argv[2]
    generate_files(id, name)

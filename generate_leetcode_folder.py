import os
import sys


language_dict = {1: "Python", 2: "SQL", 3: "Bash"}


def generate_files(id: int, name: str, language: int):

    selected_language = language_dict.get(language, None)
    file_type = ""
    code_file = ""

    if selected_language is None:
        print("Unknown Language")
        return

    # CREATE PYTHON FOLDER IF NOT EXIST
    if not os.path.exists(selected_language):
        os.makedirs(selected_language)

    # CREATE NEW LEETCODE FOLDER IF NOT EXIST
    folder_path = os.path.join(selected_language, f"[{id}]{name}")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if language == 1 and selected_language == "Python":

        # CREATE PYTHON FILE
        file_type = ".py"
        code_file = os.path.join(folder_path, f"[{id}]{name}{file_type}")
        with open(code_file, "w") as file:
            file.write("# Your Python code goes here.")

    elif language == 2 and selected_language == "SQL":

        # CREATE TEXT FILE
        file_type = ".txt"
        code_file = os.path.join(folder_path, f"[{id}]{name}{file_type}")
        with open(code_file, "w") as file:
            file.write("# Your code goes here.")

    elif language == 3 and selected_language == "Bash":

        # CREATE TEXT FILE
        file_type = ".txt"
        code_file = os.path.join(folder_path, f"[{id}]{name}{file_type}")
        with open(code_file, "w") as file:
            file.write("# Your code goes here.")

    # CREATE README.MD FILE
    readme_file = os.path.join(folder_path, "README.md")
    readme_content = f"""
# {name}

Difficulty: [EDIT HERE]

# Question Description

[EDIT HERE]

# Solution

[{name}]([{id}]{name}{file_type})

    """
    with open(readme_file, "w") as file:
        file.write(readme_content)

    print(f"Files '{code_file}' and '{readme_file}' generated successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_leetcode_folder.py <id> <name> <language>")
        sys.exit(1)

    id = sys.argv[1]
    name = sys.argv[2]
    language = int(sys.argv[3])
    generate_files(id, name, language)

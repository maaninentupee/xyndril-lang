import os

def replace_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('CoreFlux', 'CoreFlux')

    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Updated: {file_path}")

def walk_and_replace(directory):
    for root, _, files in os.walk(directory):
        for name in files:
            if name.endswith(('.py', '.md', '.nx', '.txt', '.json', '.yaml', '.yml')):
                replace_in_file(os.path.join(root, name))

if __name__ == "__main__":
    walk_and_replace(".")


import os

def get_project_structure(path):
    structure = ""
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = '  ' * level
        structure += f"{indent}- {os.path.basename(root)}/\n"
        subindent = '  ' * (level + 1)
        for f in files:
            structure += f"{subindent}- {f}\n"
    return structure

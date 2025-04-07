from pathlib import Path
import json
import os

def find_file_pathlib(filename, search_path):
    for file in Path(search_path).rglob(filename):
        return str(file)
    return None

def file_add(filename, path='C:/'):
    if os.path.exists('paths.json'):
        with open('paths.json', 'r', encoding='utf8') as f:
            try:
                paths = json.load(f)
            except Exception:
                paths = {}

    paths.update({f'{filename}': f'{find_file_pathlib(filename, path)}'})
    
    with open('paths.json', 'w', encoding='utf8') as file:
        json.dump(paths, file, ensure_ascii=False, indent=4)
    return 




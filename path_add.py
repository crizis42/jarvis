from pathlib import Path

def find_file_pathlib(filename, search_path):
    for file in Path(search_path).rglob(filename):
        return str(file)
    return None

def file_add(filename, path='C:/'):
    f = open('paths.txt', 'a')
    f.write(find_file_pathlib(filename, path) + '\n')
    return 







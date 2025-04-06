import os
import subprocess as sp
from path_add import find_file_pathlib, file_add
from time import sleep
import json


def search_in_file(file_path, search_term):
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file:
            if search_term in line:
                return True
    return False

def open_file(file_path):
    os.startfile(file_path)

def file_opening(): 
    name = input('Enter program name: ').capitalize() + '.exe'
    with open('paths.json', 'r', encoding='utf8') as file:
        paths = json.load(file)
        file_data = search_in_file('paths.json', name)
        if file_data == True:
            open_file(paths[name])
        else:
            if input('Want you to add a file? (y/n) ') == 'y':
                try:
                    file_add(name, path='C:/')
                    print('File added succefully!')
                    sleep(1)
                    with open('paths.json', 'r', encoding='utf8') as f:
                        paths = json.load(f)
                    open_file(paths[name])
                except Exception:
                    print('File does not exist')

file_opening()

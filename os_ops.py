import os
import subprocess as sp
from path_add import find_file_pathlib, file_add


def search_in_file(file_path, search_term):
    with open(file_path) as file:
        for line in file:
            if search_term in line:
                return [True, line[:-1]]
    return [False, 0]

def open_file(file_path):
    os.startfile(file_path)


file_data = search_in_file('paths.txt', input('Prog name: '))
if file_data[0] == True:
    open_file(file_data[1])
else:
    if input('Want you to add a file? (y/n)') == 'y':
        try:
            file_add(input('What is name of file?'), path='C:/')
            print('File added succefully!')
        except Exception:
            print('File does not exist')



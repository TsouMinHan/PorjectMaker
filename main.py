import datetime
import json
import os
import subprocess
import time
from pathlib import Path


def get_project_name():
    return input('Insert Your Project Name: ')

def create_venv_or_not() -> bool:
    while True:
        response = input('Do you need to create new venv? (y/n): ')
        if response == 'y':
            return True
        elif response == 'n':
            return False

def write_into_file(file, txt):
    check_folder(file.parent)

    if 'json' in file.name:
        with open(file, 'w', encoding='utf8') as f:        
            json.dump(txt, f)
    else:
        with open(file, 'w', encoding='utf8') as f:        
            f.write(txt)

def check_folder(folder_path):
    if not folder_path.exists():
        Path.mkdir(folder_path, parents=True)

def create_file(dictionary, res):
    # chanegeLoag.txt
    log_file = dictionary.joinpath('changeLog.txt')
    sentence = datetime.datetime.now().strftime("%Y.%m.%d")
    sentence += '\n開啟專案'
    write_into_file(log_file, sentence)

    # .gitignore
    txt = ".vscode\n__pycache__\nvenv"
    ignore_file = dictionary.joinpath('.gitignore')
    write_into_file(ignore_file, txt)

    # TODO
    write_into_file(dictionary.joinpath('TODO'), '')

    # main.py
    write_into_file(dictionary.joinpath('main.py'), '\n\nif __name__ == \'__main__\':\n\tpass')

    # test/test.py
    write_into_file(dictionary.joinpath('test', 'test.py'), '\n\nif __name__ == \'__main__\':\n\tpass')

    # .vscode/settings.json
    if res:
        interpreter_path = str(dictionary.joinpath(r'venv\Scripts\python.exe'))
    else:
        interpreter_path = r'D:\python\python.exe'
    dc = {
        "python.pythonPath": interpreter_path
    }
    write_into_file(dictionary.joinpath('.vscode', 'settings.json'), dc)
    
    # .vscode/launch.json
    dc = {
            "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
    }
    write_into_file(dictionary.joinpath('.vscode', 'launch.json'), dc)

def go_to_directory(directory):
    os.chdir(directory)

def create_venv():
    subprocess.call(['py', '-m', 'venv', 'venv'])
    time.sleep(2)
    subprocess.call([r'venv\Scripts\activate.bat'])
    time.sleep(0.3)
    subprocess.call(['python', '-m', 'pip', 'install', '--upgrade', 'pip'])
    time.sleep(1)
    subprocess.call([r'venv\Scripts\deactivate.bat'])

def init_git():
    subprocess.call(['git', 'init'])

    subprocess.call(['git', 'add', '.'])

    subprocess.call(['git', 'commit', '-m', '"開始專案"'])

if __name__ == '__main__':
    """
    input project name

    set python.exe's path

    create file

    create folder

    init git
    """
    project_name =  get_project_name()
    dictionary = Path().cwd().parent.joinpath(project_name)

    res = create_venv_or_not()
    create_file(dictionary, res)

    go_to_directory(dictionary)

    if res:
        create_venv()
    
    init_git()

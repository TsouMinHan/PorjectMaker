from pathlib import Path
import datetime
import json
import subprocess, os

def get_project_name():
    return input('Insert Your Project Name: ')

def set_interpreter_path():
    res = eval(input('Insert Project Interpreter\'s path(Number = default): '))
    return res if isinstance(res, str) else "D:\\python\\python.exe"

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

def create_file(dictionary, interpreter_path):
    # chanegeLoag.txt
    log_file = dictionary.joinpath('changeLog.txt')
    sentence = datetime.datetime.now().strftime("%Y.%m.%d")
    sentence += '\n開啟專案'
    write_into_file(log_file, sentence)

    # .gitignore
    txt = ".vscode\n__pycache__"
    ignore_file = dictionary.joinpath('.ignore')
    write_into_file(ignore_file, txt)

    # TODO
    write_into_file(dictionary.joinpath('TODO'), '')

    # main.py
    write_into_file(dictionary.joinpath('main.py'), '\n\nif __name__ == \'__main__\':\n\tpass')

    # test/test.py
    write_into_file(dictionary.joinpath('test', 'test.py'), '')

    # .vscode/settings.json
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

def init_git(project_name):
    os.chdir(project_name)
    command = "git init"
    subprocess.call(['git', 'init'])

    command = "git add ."
    subprocess.call(['git', 'add', '.'])

    command = 'git commit -m "專案開始"'
    subprocess.call(['git', 'commit', '-m', '"專案開始"'])

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

    interpreter_path = set_interpreter_path()

    # create_folder(project_name)
    create_file(dictionary, interpreter_path)
    
    init_git(dictionary)

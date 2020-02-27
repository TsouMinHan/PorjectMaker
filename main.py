import yaml
import json
from datetime import datetime
from pathlib import Path
import subprocess
import time 
import os

def choose_file():
    txt = 'Please choose one file which you would like to create?\n'
    file_ls = []
    for i, path in enumerate(sorted(Path('mode').rglob('*.yaml'))):
        txt += f'({i+1}) {path.name}\n'
        file_ls.append(path.name)

    try:
        num = eval(input(txt))
    except:
        print('Input number plz.')
        return None

    return Path('mode').joinpath(file_ls[num-1])

def go_to_directory(directory, project_name):
    directory = Path(directory).joinpath(project_name)
    check_folder(directory)
    os.chdir(directory)

def get_today():
    return datetime.now().strftime("%Y.%m.%d")

def get_project_name():
    return input('Insert Your Project Name: ')

def check_folder(folder_path):
    if not folder_path.exists():
        Path.mkdir(folder_path, parents=True)

def write_into_file(file, txt):
    file = Path(file)
    check_folder(file.parent)

    if 'json' in file.name:
        with open(file, 'w', encoding='utf8') as f:        
            json.dump(txt, f)
    else:
        with open(file, 'w', encoding='utf8') as f:        
            f.write(txt)

def create_venv():
    try:
        subprocess.call(['py', '-m', 'venv', 'venv'])
    except:
        print('create_venv has some prombles.')

def init_git():
    subprocess.call(['git', 'init'])

    subprocess.call(['git', 'add', '.'])

    subprocess.call(['git', 'commit', '-m', '"開始專案"'])


if __name__ == '__main__':
# version 2.0.1
    file = choose_file()

    if file:        
        with open(file, "r", encoding='utf8') as stream:
            data = yaml.load(stream)

        project_name =  get_project_name()
        
        directory = data.get('directory', Path.cwd())
        go_to_directory(directory, project_name)

        if data.get('venv', ''):
            create_venv()

        for k in data.get('create_file', []):
            content = k['content']
            if 'get_today' in content:
                content = content.replace('get_today', get_today())
            try:
                write_into_file(k['name'], content)
            except Exception as e:
                print(e)

        if data.get('git', '') and data['git'] == 1:
            init_git()
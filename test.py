from main import create_project

copy_path = "C:\Users\Tsou\Desktop\program\python\PorjectMaker\mode\Python\normal"


create_project(
    copy_path, 
    "test",
        {
            'install requests, bs4': ['pip install requests', 'pip install bs4'],
            'freeze requirements': ['pip freeze > requirements.txt'], 
            'create venv': ['python -m venv venv']
        }
    )
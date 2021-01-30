from pathlib import Path
import eel
import shutil
import json
import os
from typing import List

eel.init("web")
root_directory = Path.cwd()
package_path = Path(root_directory, "package_list.json")

@eel.expose
def modify_package_list(id: str, obj):
    data = get_project_package()
    data[id] = obj
    save_to_json(package_path, data)

@eel.expose
def delete_from_package_list(id: str):
    data = get_project_package()
    del data[id]
    save_to_json(package_path, data)

def save_to_json(path, data):
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)

@eel.expose
def insert_to_package_list(obj: dict):
    data = get_project_package()
    for i in range(len(data)+1):
        if not data.get(str(i)):
            data[str(i)] = {
                "name": obj["name"],
                "command": [cmd.strip() for cmd in obj["command"].split(",")],
                "targets": [target.strip() for target in obj["targets"].split(",")]
            }
    save_to_json(package_path, data)

@eel.expose
def create_project(copy_path: str, project_name: str, project_package_list: List[object]=[]):
    # parject_path = Path(Path.cwd(), project_name)
    # shutil.copytree(Path(copy_path), parject_path)
    # os.chdir(parject_path)

    if project_package_list:
        for cmd_ls in project_package_list:
            print(cmd_ls)
            # for cmd in cmd_ls:
                # os.system(cmd)

    os.system("git init && git add . && git commit -m \"start project\"")
    os.chdir(root_directory)

    return f"{project_name} 建立完成"

@eel.expose
def get_project_package():
    with open(package_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    return data

@eel.expose
def get_project_options():
    result_ls = []

    for mode_path in Path("mode").iterdir():
        if mode_path.is_dir():
            for project_path in mode_path.iterdir():
                dc = {
                    "language": mode_path.name,
                    "name": project_path.name,
                    "path": str(project_path),
                }
                result_ls.append(dc)
    
    return result_ls

@eel.expose
def show_window(html: str, port: int = 0, size: tuple = (800, 600)) -> None:
    try:
        eel.start(f"{html}.html", size=size, port=port)

    except (SystemExit, MemoryError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    show_window("main", size=(400, 500))
    # show_window("package_list", size=(800, 600))
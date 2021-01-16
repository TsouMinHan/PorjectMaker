from pathlib import Path

import eel

eel.init("web")

@eel.expose
def get_project_options():
    result_ls = []

    for mode_path in Path("mode").iterdir():
        if mode_path.is_dir():
            for project_path in mode_path.iterdir():
                dc = {
                    "language": mode_path.name,
                    "name": project_path.name,
                }
                result_ls.append(dc)
    
    return result_ls

def show_window(html: str, port: int = 0, size: tuple = (400, 500)) -> None:
    try:
        eel.start(f"{html}.html", size=size, port=port)

    except (SystemExit, MemoryError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    show_window("main")
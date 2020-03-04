# ProjectMaker

You can write all the files you need in the `.yaml` file, and put it in the `mode` folder.
Create project folder with this script.

## .yaml exaple
- `create_file`: create the files

- `name`: file name

- `content`: The content of the file. It can be a string or json.

(if you need current date, write the code `get_today`)

(if you do not need anything, write '')

- `git`: initialize the git repository, write 1

- `directory`: your project parent directory

- `cmd`: bash code.

```yaml
create_file:  
  - name: chanegeLoag.txt
    content: |
      get_today
      專案開始
  - name: .gitignore
    content: |
      .vscode
      __pycache__
      venv
  - name: TODO
    content: ''
  - name: app.py
    content: |
    
    
      if __name__ == '__main__':
          pass
  - name: test/test.py
    content: |
      

      if __name__ == '__main__':
          pass
          
  - name: .vscode/settings.json
    content: 
      {
        "python.pythonPath": "D:\\python\\python.exe"
      }

  - name: .vscode/launch.json
    content: 
      {
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
  - name: static/js/index.js
    content: ''
  - name: static/css/index.css
    content: ''
  - name: main/__init__.py
    content: ''
  - name: templates/index.html
    content: ''
git: 1
directory: D:\pyCharm
cmd: py -m venv venv
```
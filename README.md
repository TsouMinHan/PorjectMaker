# ProjectMaker
將需要的檔案寫入`.yaml`檔案，放到`mode`資料夾，接著執行主程式，就可以產生寫入的檔案。

目前有
1. Flask所需檔案
2. PyQt所需檔案
3. 一般專案所需檔案

You can write all the files you need in the `.yaml` file, and put it in the `mode` folder.
Create project folder with this script.

Current base project
1. Flask required files
2. PyQt required files
3. Normal project required files

## .yaml exaple
- `create_file`: 要創建的檔案要在此縮排內。

- `name`: 檔案名稱。

- `content`: 檔案的內容(可以是json)。

(如果需要取得當前日期，可以在content內輸入`get_today`。)

(若不需要任何內容，請輸入''。)

- `git`: 輸入1代表需要初始git，其他則否。

- `directory`: 設定專案路徑

- `cmd`: 輸入cmd指令


- `create_file`:  the file to be created must be in this indent.

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

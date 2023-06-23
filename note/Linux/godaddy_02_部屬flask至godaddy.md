# 部屬flask至godaddy
http://benincampus.blogspot.com/2020/09/setting-godaddy-hosted-site-to-use.html

https://github.com/nicholasvad/flask_on_godaddy

https://www.youtube.com/watch?v=260eDcsUheE

這裡主要是建立flask，他採用的並非子網域，而是path, 就是網址最後的斜線之後


## 1.使用cPanel建立ptyohn
```
1.1 進入頁面 登入godaddy主頁 > cPanel > Software > Setup Python App
1.2 建立python app  按下 CREATE APPLICATION
1.3 選擇python版本，選擇最新即可
1.4 Application root 程式跟目錄名稱，輸入test_flask
1.5 Application URL 是網址後方的首個path，輸入test_flask
1.6 Application startup file 啟動檔案,輸入app.py
1.7 Application Entry point app進入點，通常是啟動檔案的app變數, 輸入app
1.8 Passenger log file log檔案為必須，輸入logs/test_flask.log
1.9 輸入完畢後按下 CREATE

```

## 系統自動建立資料夾 (使用者不用建立)
1. 使用者跟目錄底下建立 test_flask資料夾  專門用來放置程式
2. 使用者跟目錄底下建立 virtualenv資料夾  專門用來放置虛擬環境
3. public_html底下建立 test_flask資料夾  專門用來放置網web配置(.htaccess)

## 2.檢查
2.1 檢查 在頁面Application URL 右方 按下open將打開網址http://selecter.org/test_flask，檢查是否正常
2.2 在cPanel 我們可以看到python app已經正在運作，並且有STOP APP及 RESTARE按鈕
2.3 若我們使用putty輸入top，就可看到多了一個python線程

## 3.在虛擬環境安裝套件
3.1 進入到 WEB APPLICATIONSSELECTER.ORG/TEST_FLASK 頁面
3.2 安裝之前一定要先停止線程，在app頁面 按下STOP APP
3.3 使用cPanel File Manager 來操作,在~/test_flask目錄底下建立requirements.txt，他是裝門用來紀錄虛擬環境所需套件及版本的文件。
3.4 編輯 requirements.txt，在此輸入Flask==2.3.2
3.5 回到 WEB APPLICATIONSSELECTER.ORG/TEST_FLASK 頁面 拉到下方Configuration files
3.6 輸入 requirements.txt 按下右側Add 即加入上方的候選名單中
3.7 上方run pip install 下拉選單 選擇剛才輸入的requirements.txt 將進行安裝，安裝完成後將顯示成功安裝。在此我們已經成功安裝flask
3.8 檢查虛擬環境，使用cPanel File Manager檢查 virtualenv//TEST_FLASK 底下的套件發現已經安裝上了flask

## 4.修改原始的app.py 及 app
4.1 將以下內容覆蓋掉原始的app.py
4.2 WEB APPLICATIONSSELECTER.ORG/TEST_FLASK 頁面按下START APP
4.3 開啟頁面檢查

```python 原始內容
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python v' + sys.version.split()[0] + '\n'
    response = '\n'.join([message, version])
    return [response.encode()]

```

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

```
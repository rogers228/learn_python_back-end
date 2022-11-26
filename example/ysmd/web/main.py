from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



# 開發環境使用 flask內建的 Werkzeug 作為server啟動  進行調試
# cmd
# cd /d C:\Users\user\Desktop\ysmd\web
# set FLASK_APP=main
# set FLASK_ENV=development
# flask run --port=8239          啟動app server
# 瀏覽器上運行 http://127.0.0.1:8239/
# or
# flask run --port=8239 --cert=adhoc  使用臨時憑證 SSL
# 瀏覽器上運行 https://127.0.0.1:8239/




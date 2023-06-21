# 子網域
用 store.yoursite.com 舉例說明，在這個範例內，store 就是子網域，yoursite 是主要網域，而 .com 則是頂級網域 (TLD)。
(以下尚未驗證)

一個網域名稱最多可設定 500 個子網域。您也可以為子網域加入多個階層，如 info.blog.yoursite.com。子網域最長可以設定 255 的字元，不過如果子網域有多個階層，則每個階層只能使用 63 個字元。

## 新增子網域 就是 管理DNS

1. 進入 godaddy登入 > 所有產品與服務 > 網域 > 管理 > 左側選單網域 > 找到網域 > 管理DNS
2. 左側網域組合 > 找到網域 點選...符號 > 編輯DNS > 新增記錄, 
    類型選擇A, 
    名稱：子網域的主機名稱或前綴。例如，您可以輸入 blog，即可建立 blog.mycoolnewbusiness.com 的子網域。
    內容值：子網域的 IP 位址。這通常是您主機服務帳戶的 IP 位址。
    TTL：伺服器快取資訊的時間長短。預設為 1 小時。

## 子網域對應資料夾

1. 若主網域為selecter.org
2. 若建立子網域`tf` 則網址為tf.selecter.org
3. 若建立子網域`tf` 對應的資料夾為 `/home/vqpcm2y2n0qr/public_html/tf.selecter.org`

## 建立資料夾
```
cd ~
cd public_html
mkdir tf.selecter.org   建立資料夾
cd tf.selecter.org
mkdir cgi-bin   建立cgi資料夾
```

## 安裝python虛擬環境
```
python3 -m pip install virtualenv  # 安裝 virtualenv
virtualenv -p /home/vqpcm2y2n0qr/.local/bin/python3 venv # 指定虛擬環境的python解釋器，這將會建立虛擬venv資料夾，及相關檔案
source venv/bin/activate  # 啟動虛擬環境   命令列將以(venv)開頭代表目前進入虛擬環境
python3 -m pip list  # 查詢目前的虛擬環境的套件
python3 -m pip install Flask   # 安裝必要套件
deactivate  # 退出虛擬環境
```

## 建立cgi檔案
建立/home/vqpcm2y2n0qr/public_html/tf.selecter.org/cgi-bin/app.cgi

```python
#!/home/vqpcm2y2n0qr/.local/bin/python3
import os
import sys
sys.path.insert(0,
                '/home/vqpcm2y2n0qr/public_html/tf.selecter.org/venv/lib/python3.10/site-packages')
from wsgiref.handlers import CGIHandler
from app import app
class ProxyFix(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        environ['SERVER_NAME'] = ""
        environ['SERVER_PORT'] = "80"
        environ['REQUEST_METHOD'] = "GET"
        environ['SCRIPT_NAME'] = ""
        environ['QUERY_STRING'] = ""
        environ['SERVER_PROTOCOL'] = "HTTP/1.1"
        return self.app(environ, start_response)
if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CGIHandler().run(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
CGIHandler.run(app)
```

## 建立app.py
建立 /home/vqpcm2y2n0qr/public_html/tf.selecter.org/cgi-bin/app.py:
```python
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
```

## 建立首頁
建立 templates 資料夾，建立home.html，並且輸入一些內容， 位於cgi-bin/templates/home.html

## 設定Apache的配置文件
建立.htaccess
位於/home/vqpcm2y2n0qr/public_html/tf.selecter.org/
內容如下
```
Options +ExecCGI 
AddHandler cgi-script .py
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f 
RewriteRule ^(.*)$ /home/vqpcm2y2n0qr/public_html/tf.selecter.org/cgi-bin/app.cgi/$1 [L]
```

RewriteRule ^(.*)$ /home/USERNAME/public_html/python/cgi-bin/app.cgi/$1 [L]


主要是讓apache配置可以套用到app.cgi

## 設定權限
將當前目錄下的所有文件和文件夾的權限設置為：所有者俱有讀、寫和執行權限，所屬組和其他用戶具有讀和執行權限，即常用的默認權限設置。
```
cd /home/vqpcm2y2n0qr/public_html
chmod 755 *
```

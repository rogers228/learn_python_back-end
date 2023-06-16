# 開發環境 使用 werkzeug (flask內建的專門debug的服務器)

import os, sys
from werkzeug.serving import run_simple
from web_config import *

# sys.path.append(PATH_FLASK)   # 加入 falsk app路徑
import web_main                   # 匯入 flask 主程序
app_server_name = 'development_for_ysmd_flask_google_login'
port = 8231

print(f'\n=========  {app_server_name} is running.  ===========')
print(f'http://localhost:{port}')

# run_simple('localhost', port, web_main.app, use_reloader=False) 不會等待連線
# run_simple('127.0.0.1', port, web_main.app, use_reloader=False) 會連線至其他網路
run_simple('0.0.0.0', port, web_main.app, use_reloader=False) # 可供連線
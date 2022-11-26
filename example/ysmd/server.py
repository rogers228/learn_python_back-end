from waitress import serve
from web.main import app
# from web import main

app_server_name = 'app_server_1'
port=8239

print(f'{app_server_name} is running for waitress wsgi\nport:{port}')
serve(app, host='0.0.0.0', port=port)


# 生產環境 使用 waitress wsgi server

# cmd 執行 waitress
# cd /d C:\Users\user\Desktop\ysmd
# python server.py

# http://127.0.0.1:8239
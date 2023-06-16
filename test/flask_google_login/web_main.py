import os, sys
import json
from flask import (Flask, send_file, make_response)
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # 設定為 cors
app.config.from_pyfile('web_config.py')
config = app.config.get

# COOP
@app.before_request
def set_cross_origin_opener_policy():
    response = make_response()
    response.headers['Cross-Origin-Opener-Policy'] = 'flask_test_google_login'
    
@app.route("/")
def index():
    return send_file(config('FILE_INDEX'))


def test1():
    print(config('S_TEST'))

if __name__ == '__main__':
    test1()
# 在工作站執行linux python

在windows工作站直接執行linux python，
這是一個高級技巧，直接在工作站windows直接執行linux python，不需要透過putty

## 工作原理
1. 在linux 先建立好python環境，請參閱 godaddy_04_python虛擬環境.md
2. 建立php 供外部請求，php內使用shell_exec()，直接指定python環境，執行python腳本
3. 在工作站 建立請求python腳本


```php
<?php

if (true){ // setting
    require 'apikey.php';        // 引用 config
    date_default_timezone_set('Asia/Taipei'); // 設定 時區
    error_reporting(E_ALL);       // 設定 顯示所有錯誤
    ini_set('display_errors', 1); // 設定 顯示錯誤
    header('Content-Type: application/json'); // 設定 header 返回資料格式為 json
    $current_time = date('Y-m-d H:i:s');
}

if (true){ // 驗證 API 密鑰
    if (!isset($_GET['api_key']) || $_GET['api_key'] !== API_KEY) {
        error_log('api key error, ' . date('Y-m-d H:i:s')); // output error
        http_response_code(401); // 權限不足
        exit(0); // 離開
    }
}

$output = shell_exec('/home/vqpcm2y2n0qr/virtualenv/python311/3.11/bin/python /home/vqpcm2y2n0qr/python311/test1.py');
$result = [
    'message' => 'hi, i am php.',
    'output' => $output,
    'time' => $current_time,
];
echo json_encode($result); // 返回 JSON 格式的數據

?>
```


```python
import requests
import json

def test1():
    print('request...')
    url = 'https://selecter.org/webapp/phpython.php?api_key='
    response = requests.post(url)
    result = json.loads(response.text)
    print(result)
    print(type(result))

if __name__ == '__main__':
    test1()
```
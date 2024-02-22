cmd
移動到目錄
cd /d C:\Users\user\nginx-1.23.0

檢查版本
nginx -v

啟動
start nginx

檢查工作管理員是否啟動
tasklist /fi "imagename eq nginx.exe"

關閉
nginx -s stop

重新讀取 載入
nginx -s reload

檢查配置
nginx -t -c conf\nginx.conf
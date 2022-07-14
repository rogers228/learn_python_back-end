https://rookiesavior.net/2022/04/20/program-yiru-web-server-nginx-implementation-on-windows/

Nginx
1.到官網下載後解壓縮
2.啟動 nginx
    cmd
    cd /d C:\Users\user\nginx-1.23.0
    start nginx
    無法啟動可能是port被占用 修改配置檔nginx.conf

http://127.0.0.1:8800/
http://localhost:8800/

檢查 nginx.conf
    cmd
    cd /d C:\Users\user\nginx-1.23.0
    nginx -t -c conf\nginx.conf

    出現以下代表配置檢查沒有問題
    nginx: the configuration file C:\Users\user\nginx-1.23.0/conf\nginx.conf syntax is ok
    nginx: configuration file C:\Users\user\nginx-1.23.0/conf\nginx.conf test is successful



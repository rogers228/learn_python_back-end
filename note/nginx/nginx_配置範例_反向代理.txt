輸入網址： client 端輸入網域 a  www.123.com
解析網址：   windows 本地 host文件查找紀錄
            若無則到網上dns 解析為host ip b
反向代理： 連接到 host ip b 主機nginx 192.168.17.129:80
          反向代理到主機內部 127.0.0.1:8080


準備工作
1.準備好app server，例如flask網站

2.開放windows防火牆 端口
  2.1 查看已經開放的端口
  2.2直接訪問app server 測試flask網站


開始
1.windows host文件 (開發用)
    可以參考
        https://www.60km.com/hosts-document/
    C:\Windows\System32\drivers\etc\hosts
    添加內容
        host(ip)  hostname(網域)
    以上已經可以執行 a->b


2.nginx反向代理設定
    
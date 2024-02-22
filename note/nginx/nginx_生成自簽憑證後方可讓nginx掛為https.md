使用OpenSSL工具生成自签名SSL证书。运行以下命令：
依照指示輸入各項屬性即可

```
cd /d C:\Users\user\Documents\Rogers\ys_yrpc\flask
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 10950

```

Country Name 國家名 TW
State or Province Name 洲或省名 Taichung
Locality Name 地區名稱 Wufeng
Organization Name 機構組織名稱 YEOSHE
Organizational Unit Name 單位名稱 RD
Common Name 通用名稱 YSRD
Email Address twa115@yeoshe.com.tw


```
    server {
        # listen       443 ssl; https預設port 當使用者不加port號時
        listen       4439 ssl;
        server_name  yrpc;

        ssl_certificate C:/Users/user/Documents/Rogers/ys_yrpc/flask/cert.pem;
        ssl_certificate_key C:/Users/user/Documents/Rogers/ys_yrpc/flask/key.pem;
        location / {
            proxy_pass http://127.0.0.1:8245;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
```
.htaccess
```
# 禁止跨域 iframe
<IfModule mod_headers.c>
    Header set X-Frame-Options "SAMEORIGIN"
</IfModule>
```
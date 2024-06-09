# url重寫
是網址對應到實際的路徑或條件

1. 美化url
2. 改善sel


# 注意事項
1. SEO sitemap 應使用 url 重寫的路徑，非原始路徑
2. 引用的js如果使用相對路徑，將相對於url，有可能錯誤，故建議改為絕對路徑


## 如何使用
在跟目錄建立`.htaccess`

```
# 啟用 URL 重寫引擎
RewriteEngine On
RewriteRule ^test$ test_php/ZFHxgESDRiG0_en.html [L]
```
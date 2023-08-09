# 環境變數


## 常用指令
```sh
printenv 列出所有環境變數
echo $PATH  列出環境變數

export PASSWORD="your_password_here"
password=$PASSWORD 將環境變數儲存在變數
echo "Password is: $password" 使用變數

unset VARIABLE_NAME  刪除環境變數
```

## 使用者輸入變數
```sh
echo "請輸入您的名稱："
read username
echo "您好，$username！歡迎使用本程式。"

echo "請輸入您的密碼："
read -s password


echo "您輸入的密碼是：$password"

```
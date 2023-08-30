#cronjob
工作任務，由godaddy cronjob 定期執行

## 注意事項
1. 當cronjob執行工作時，角色視為其他人，故須注意權限(資料夾及檔案)
2. 當cronjob執行工作時，任何路徑應使用絕對路徑

```bash
# 查看所有工作
crontab -l

# 列出權限
ls -lR /home/vqpcm2y2n0qr/practice/MS_66_api/villa/test_cronjob

#output.log要將權限從`-rw-rw-r--`設定為`-rw-rw-rw-``,設定output.log 其他人可以寫
chmod o+w output.log

# 設定目錄其他人可以寫
chmod o+w /home/vqpcm2y2n0qr/practice/MS_66_api/villa/test_cronjob

```

## 自動傳送結果到email
系統將傳送最後一個print()至email

```bash
#抑制傳送email, 命令後方加入以下
 mycommand >/dev/null 2>&1
```


## 其他
```bash
date # 目前日期時間

```

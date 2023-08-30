# nohup
執行後台腳本的命令，
通常可以搭配 Cron job (定時任務)
使用Cronjob 固定開啟腳本 在背景執行python3，監控任務

man nohub 查看幫助
q 退出

nohup python3 background_script.py
nohup python3 background_script.py > output.log 2>&1 &
背景執行腳本
2>&1 輸入至log
& 背景執行獨立運作

ps      查看目前工作
ps aux  查看目前工作 詳細資料
ps aux | grep python3    查看 python3 所開啟的進行
pgrep -f your_script.py  以執行檔案查看pid

kill 284980       關閉線程 pid

cat output.log

# 將linux資料夾push至github

## 1. 由linux為起點 建立github

有時候linux server 所建立的資料夾，是工作的起點，並非windows工作站為起點，故首次建立需要從linux操作

1. 至github網站建立一個空白github倉庫
2. 移動至資料夾 cd test_flask 初始化 git init   這將建立.git資料夾
3. 將目錄下所有文件添加至暫存區  git add .
4. 將暫存區的資料提交 git commit -m "Initial commit"
5. 設定當前分支的重新命名為main  git branch -M main
6. 將當前資料夾連線  git remote add origin git@github.com:rogers228/test_flask.git
7. 推送 git push -u origin main
8. 至github檢查是否內容已經推送上去

以上就完成了由linux為起點，push至github

## 2. 在windos工作站 clone 倉庫 及工作

1. 使用GitHub Desktop 非常方便
2. add > clone repository > 選擇剛才的倉庫，這樣就建立完成了
3. 平常在工作站編程，push

## 3. 更新linux

1. cd 移動到資料夾
2. git pull 同步  並輸入密碼
3. 若是有更新主程序(例如app.py)，必須重新啟動python app才會生效
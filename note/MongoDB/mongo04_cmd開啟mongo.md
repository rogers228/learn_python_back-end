# cmd開啟mongo

## 指定資料庫路徑啟動mongo
系統管理員身分執行cmd
以指定資料庫路徑啟動 mongo
此視窗非服務不可關閉
後續使用MongoDB Compass介面需依靠mongo 才能跑
需先設定環境變數

```cmd
mongod --dbpath "C:\Program Files\MongoDB\Server\6.0\data"
```

後續方可以用mongodb
例如:mongodb compass, flask, svelte, 瀏覽器


## 常用路徑
程式安裝路徑
C:\Program Files\MongoDB

加入系統環境變數
C:\Program Files\MongoDB\Server\6.0\bin

預設資料庫路徑
C:\Program Files\MongoDB\Server\6.0\data
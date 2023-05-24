# 將備份的資料還原到server

mongorestore 




mongorestore 是 MongoDB 的一個命令行工具，用於將使用 mongodump 工具創建的備份資料還原到 MongoDB 數據庫中。它可以將 BSON 或 JSON 格式的備份文件還原成 MongoDB 中的數據集合。

以下是 mongorestore 命令的基本語法：

--host：指定 MongoDB 服務器的主機名或 IP 地址。
--port：指定 MongoDB 服務器的端口號。
--username 和 --password：指定連接 MongoDB 服務器的用戶名和密碼。
--authenticationDatabase：指定用於身份驗證的數據庫。
--db：指定要還原的數據庫名稱。
--collection：指定要還原的集合名稱。
--drop：在還原之前刪除目標集合。
--gzip：還原壓縮的備份文件。
--dir：指定要還原的目錄路徑，用於還原整個數據庫。


還原整個備份目錄：
```
mongorestore --host localhost --port 27017 --dir /path/to/backup/directory
```

還原特定數據庫：
```
mongorestore --host localhost --port 27017 --db mydatabase /path/to/backup/directory
```

還原特定集合：
```
mongorestore --host localhost --port 27017 --db mydatabase --collection mycollection /path/to/backup/file.bson
```
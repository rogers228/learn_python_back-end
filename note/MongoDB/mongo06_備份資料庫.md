## 資料庫備份
mongodump

```
mongodump --db "pnssdb" --out "C:\mongodb_backup\20230524"
```


mongodump 是 MongoDB 提供的一個工具，用於將資料庫中的資料備份到本地文件系統。以下是 mongodump 命令的說明：


--uri=<connection-string>：使用指定的連接字串來連接 MongoDB 服務器。
--host=<hostname>：指定 MongoDB 服務器的主機名或 IP 地址。
--port=<port>：指定 MongoDB 服務器的連接埠。
--username=<username>：指定用於身份驗證的使用者名稱。
--password=<password>：指定用於身份驗證的密碼。
--out=<directory>：指定備份文件的輸出目錄。
--gzip：將備份文件以 gzip 壓縮格式進行壓縮。
--archive=<file>：將備份文件輸出到壓縮存檔文件。
--db=<database>：指定要備份的資料庫。
--collection=<collection>：指定要備份的集合。
--query=<json>：指定備份時的查詢條件，只備份符合條件的文件。
--ssl：使用 SSL 連接到 MongoDB 服務器。
--authenticationDatabase=<database>：指定用於身份驗證的資料庫。
使用 mongodump 命令可以根據需要進行各種選項的設定，以執行適當的資料備份作業。備份的資料可以使用 mongorestore 命令進行還原到 MongoDB 伺服器中。
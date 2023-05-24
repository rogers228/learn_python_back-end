# 設定Server為服務

以系統管理權限執行
```
mongod.exe --install --serviceName "MongoDB_ys" --serviceDisplayName "MongoDB_ys" --dbpath "C:\Program Files\MongoDB\Server\6.0\data" --logpath "C:\Program Files\MongoDB\Server\6.0\log\mongod.log" --logappend
```

上述命令中的參數可以根據你的系統和需求進行調整，下面是一些常見的參數解釋：

--serviceName：指定服務的名稱，這裡設置為 "MongoDB"，你可以根據需要自定義名稱。
--serviceDisplayName：指定在服務管理器中顯示的服務名稱，這裡設置為 "MongoDB"，你可以根據需要自定義顯示名稱。
--dbpath：指定 MongoDB 數據庫文件的存儲路徑，這裡設置為 "C:\data\db"，你可以根據需要自定義路徑。
--logpath：指定 MongoDB 日誌文件的存儲路徑，這裡設置為 "C:\data\log\mongod.log"，你可以根據需要自定義路徑。
--logappend：指定日誌文件是否添加到現有文件的末尾，這樣可以保留先前的日誌內容。
--directoryperdb：將每個數據庫存儲在單獨的目錄中。



## 開啟服務

開始>控制台>系統及安全性>系統管理工具>服務
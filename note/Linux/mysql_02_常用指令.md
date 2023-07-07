## 常用資料類型
以下為常用資料類型，一般已經足夠了
1. CHAR(14) 固定長度字串
2. TEXT 備註類
3. INT 整數
4. DECIMAL(4, 2) 第一個參數為總位數(包括小數點)，第二個為小數保留幾位

## 其他資料類型
1. DATETIME  日期時間，通常使用CHAR(14) 就很好用了
2. TIMESTAMP  時間戳記, 另一種的時間表示
3. BOOLEAN    0 = FALSE 1 = TRUE  BOOL也是同義

## 建立資料表
```
CREATE TABLE rec_rpn
(rp01 int PRIMARY KEY,
rp02 int,
rp03 varchar(50),
rp06 text,
rp07 int,
rp08 text,
rp09 datetime)
```

## 查詢筆數
```
SELECT ts01, ts02 FROM rec_test LIMIT 10
```
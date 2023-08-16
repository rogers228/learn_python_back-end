https://shubo.io/cookies/
# cookie
看似object實則不然，有自己的一套規則，需要另外學習。

## 基礎概念
1. 後端控制： cookie通常由後端控制, 前端可以使用`console.log(document.cookie)`來查看目前cookie(僅name value)
2. 無刪除： cookie無刪除的概念，僅有過期的概念，所以當你查看時它依然存在，故應當查看expires(有效時間)
3. 安全性: 除了name, value, 可供前後端讀取，其餘的參數因為安全性無法直接讀取。 所以的資料應用僅能在name, value

## 參數
- name
- value
- expires 失效時間 (過期時間之前為有效時，之後為無效)
- max_age 保存時間 (保存多久後就失效)
- max_age 和 expires 是對應個 cookie 非個別key，你只需要設定其中一個即可，兩者是互斥的。
- domain 網域
- path 路徑    path='/' 代表全站
- secure secure=True    限制 https
- httponly httponly=False  僅http 防止JavaScript 存取cookie
- samesite   strict | lax | none  strict 網域相同才會發送這個 cookie

## 偵錯
- 使用無痕視窗
- 使用控制台查看cookie

## 注意事項
1. 操作cookie的控制通常是後端，有能是python flask, php, node javascript, 網路上的範例通常是javascript，所以不要誤會是前端控制

https://shubo.io/cookies/
# cookie
看似object, key value 實則不然，有自己的一套規則，需要另外學習。

## 基礎概念
1. 後端控制： cookie通常由後端控制, 前端可以使用`console.log(document.cookie)`來查看目前cookie(僅name value)
2. 無刪除： cookie無刪除的概念，僅有過期的概念，所以當你查看時它依然存在，故應當查看expires(有效時間)
3. 安全性: 除了name, value, 可供前後端讀取，其餘的參數因為安全性無法直接讀取。 所以的資料應用僅能在name, value
4. 後端與瀏覽器溝通: 使用cookie (respons.set_cookie,  request.cookies.get)
5. 後端與前端溝通不需仰賴cookie:   使用body (response = make_response(jsonify({'message': 'set cookie.'}))

## 角色
cookie的運作，不可僅用前端與後端來說明，會有3種角色
1. 前端javascript 為網站開發者主導
2. 後端 不一定是js, 有可能是js, php, java, go, python, c#
3. 瀏覽器自動處理cookie機制

## 瀏覽器自動處理cookie機制
cookie是靠瀏覽器機制傳送與設定，並非完全前端js控制，也非完全後端控制，
瀏覽器在發送請求，接收設定cookie，都會做把關，並不會無條件的發送或設定。

1. 前端javascript發起請求時，瀏覽器會依條件攜帶cookie 一併發送請求給後端
2. 後端收到請求，可以讀取cookie，設定cookie，回應給瀏覽器
3. 瀏覽器收到回應後，瀏覽器會再依條件設定cookie

## 參數
- name
- value
- expires 失效時間 (過期時間之前為有效時，之後為無效)
- max_age 保存時間 (保存多久後就失效)
- max_age 和 expires 是對應個 cookie 非個別key，你只需要設定其中一個即可，兩者是互斥的。
- domain 網域
- path 路徑    path='/' 代表全站
- secure secure=True    限制 https
- httponly httponly=False  僅http 防止JavaScript 存取cookie的特定key
- samesite 前端請求時瀏覽器發送cookie給後端的條件
-- strict 嚴格的: request請求的網域 必須和 目前網址的網域 相同 才會發送cookie給後端
-- lax    鬆懈的: 同上，除了get導向相同網域(目前尚未使用到)
-- none   無管制: 一律發送

## 偵錯
- 使用無痕視窗
- 使用控制台查看cookie

## 注意事項
1. 操作cookie的控制通常是後端，有能是python flask, php, node javascript, 網路上的範例通常是javascript，所以不要誤會是前端控制

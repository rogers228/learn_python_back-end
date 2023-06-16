# google api

## google 登入介紹
https://developers.google.com/identity/gsi/web/guides/overview
可以切換為繁體中文，比較好閱讀

## google cloud
用來取得api
https://console.cloud.google.com/apis/dashboard?project=profound-jet-296913


## google 登入成功後的json
```
{
    "iss": "https://accounts.google.com",
    "nbf": 1686633546,
    "aud": "638367158836-tpd72604ppap28e9pirbggv2q5fca7m3.apps.googleusercontent.com",
    "sub": "113868765054760031131",
    "email": "rogers2288@gmail.com",
    "email_verified": true,
    "azp": "638367158836-tpd72604ppap28e9pirbggv2q5fca7m3.apps.googleusercontent.com",
    "name": "Rogers Lu",
    "picture": "https://lh3.googleusercontent.com/a/AAcHTteZXlhUQKl_Ozl09IgtlA0oL_tE54MZtqP5Z5gnCYk=s96-c",
    "given_name": "Rogers",
    "family_name": "Lu",
    "iat": 1686633846,
    "exp": 1686637446,
    "jti": "be51644341ad10b192e205ce7aec757d53c6d352"
}
```

```
    iss: 發行者（Issuer）的網址，表示這個 ID Token 是由哪個身份提供者發行的，這裡是 https://accounts.google.com，表示由 Google 發行。
    nbf: Not Before，表示此憑證的有效期在此時間之後才開始。
    aud: 受眾（Audience），表示此憑證的目標受眾，這裡是你在 Google 開發者控制台設定的客戶端 ID。
    sub: 主題（Subject），唯一識別此使用者的 ID。
    email: 使用者的電子郵件地址。
    email_verified: 表示電子郵件是否已經驗證。
    azp: 授權發行者（Authorized Party），表示此憑證的授權發行者，這裡是你在 Google 開發者控制台設定的客戶端 ID。
    name: 使用者的完整姓名。
    picture: 使用者的頭像圖片 URL。
    given_name: 使用者的名字。
    family_name: 使用者的姓氏。
    iat: 簽發時間（Issued At），表示此憑證的簽發時間。
    exp: 過期時間（Expiration Time），表示此憑證的有效期限。
    jti: JWT ID，表示此憑證的唯一識別碼。
```
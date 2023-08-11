import jwt

def test1():
    data = {'user': 'payload'} # 傳輸的資料
    keyword = 'df$8Td' # 加密解密金鑰
    token  = jwt.encode(data, keyword, algorithm='HS256') # 產生token暗碼 傳輸用

    # flask
    # response.headers['Authorization'] = f'Bearer {token}'
    # token 透過 headers 傳輸 避免CSRF (跨站請求偽造)
    # 前綴 Bearer 是前後端約定慣例  Bearer後方為token 全端設計時也非必要
    # 後續前端請求時，應附上token

    print(token)
    ans = jwt.decode(token, keyword, algorithms=['HS256']) # 後端解碼
    print(ans)

if __name__ == '__main__':
    test1()
import pymongo
import pandas as pd

def test1():
    dictionary_data = {
        "name": "department",
        "data": [
            {'id' : 1, 'no' : 'A001', 'name' : '研發部'},
            {'id' : 2, 'no' : 'A003', 'name' : '管理部'},
            ]
        }

    if isinstance(dictionary_data, dict):
        print("dictionary_data is a valid dictionary")
        print(dictionary_data)
        
        # 建立db 及 建立集合(資料夾) 插入(檔案)
        conn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = conn['pnssdb'] # 非直接建立db 僅會在資料建立時才會建立db
        mycol = db['basic']  # 非直接建立collection 僅會在資料建立時才會建立collection
        mycol.insert_one(dictionary_data) # 插入文件(dic)
        print('ok')

    else:
        print("dictionary_data is not a dictionary")
        

def test2():
    # 尋找 department 文件
    # 並以 dataframe 顯示
    db = pymongo.MongoClient("mongodb://localhost:27017/")['pnssdb']
    col = db['basic']
    query = {"name": "department"}
    result = col.find(query)[0] # 僅找到第一個
    if result:
        # print(result)
        lis_data = result['data']
        df = pd.DataFrame(lis_data) # 轉dataframe
        print(df)
        # # json以供傳輸
        # json_data = df.to_json(orient='records') 
        # print(json_data)
    
def test3():
    #更新資料  依照id更新
    db = pymongo.MongoClient("mongodb://localhost:27017/")['pnssdb']
    col = db['basic']
    query = {"name": "department", "data.id": 2} # 查詢條件
    update = {"$set": {"data.$.no": "A002", "data.$.name": "開發部"}} # 更新
    col.update_one(query, update)

if __name__ == '__main__':
    test2()
    print('ok')
import pymongo

def test1():
    # 所有資料庫
    myclient = pymongo.MongoClient("mongodb://localhost:27017/") # Connect to MongoDB
    dblist = myclient.list_database_names() # 所有db
    for db in dblist:
        print(db)

def test2():
    # 架構 db / collection(資料夾)
    # 查看 db 內 collecctions (集合) (資料夾)
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    db_local = conn["local"] # 非直接建立db 僅會在資料建立時才會建立db
    lis_col = db_local.list_collection_names()
    for e in lis_col:
        print(e)

def test3():
    # 建立db 及 建立集合(資料夾) 插入(檔案)
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = conn['testdb'] # 非直接建立db 僅會在資料建立時才會建立db
    mycol = mydb['developers']  # 非直接建立collection 僅會在資料建立時才會建立collection
    dic_developer = {"name": "Lini", "address": "Sweden"}
    mycol.insert_one(dic_developer) # 插入文件(dic)

def test4():
    # 列出集合內所有文件 資料夾所有檔案
    db = pymongo.MongoClient("mongodb://localhost:27017/")['testdb']
    col = db['developers']
    for doc in col.find():
        print(doc)

if __name__ == '__main__':
    test4()
    print('ok')
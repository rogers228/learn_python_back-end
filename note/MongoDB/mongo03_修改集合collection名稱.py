import pymongo

def test1():
    db = pymongo.MongoClient("mongodb://localhost:27017/")['pnssdb']
    db['department'].rename('basic') # 重新命名collection  為basic
    

if __name__ == '__main__':
    test1()
    print('ok')
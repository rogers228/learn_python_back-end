import sys, os
from supabase import create_client, Client

# 添加 GRST_PATH 路徑，匯入 global_config
sys.path.append(os.getenv('GRST_PATH'))
from global_config import OPTION

url = OPTION.get("spwr_api_url")
# print(url)
admin = OPTION.get("spwr_api_service_key")
visitor = OPTION.get("spwr_api_anon_key")
# print(visitor)


def test1():
    db: Client = create_client(url, visitor)
    response = db.table("rec_test").select("*").execute()
    data = response.data
    print(data)
    print(type(data))

def test2():
    # 查詢所有資料表
    pass

if __name__ == '__main__':
    test2()
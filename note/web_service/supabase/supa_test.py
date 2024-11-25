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
    db: Client = create_client(url, visitor)
    response = db.table('rec_test').select('ts02').like('ts01', 'A001').limit(1).execute()
    if response.data:
        print(response.data[0])
        return response.data

if __name__ == '__main__':
    test2()
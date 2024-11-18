import sys, os

# 添加 GRST_PATH 路徑，匯入 global_config
sys.path.append(os.getenv('GRST_PATH'))
from global_config import OPTION

import cloudinary
import cloudinary.uploader
import cloudinary.api
cloudinary.config(
    cloud_name = OPTION.get('cloud_name'),
    api_key = OPTION.get('cloud_api_key'),
    api_secret = OPTION.get('cloud_api_secret')
)



# 添加 GRST_PATH 路徑，匯入 global_config
sys.path.append(os.getenv('GRST_PATH'))
from global_config import OPTION

def test1():
    file_path = os.path.join(os.path.dirname(__file__), 'image1.jpg')
    # print(file_path)

    try:
        result = cloudinary.uploader.upload(file_path)
        file_id = result.get("public_id")  # 取得檔案的 ID
        file_url = result.get("url")      # 取得檔案的 URL
        print(f"檔案上傳成功！\nID: {file_id}\nURL: {file_url}")

        # ID: jnu1zysyt86hcwaavh32
        # URL: http://res.cloudinary.com/dk97nvln0/image/upload/v1731909898/jnu1zysyt86hcwaavh32.jpg

        return file_id, file_url
    except Exception as e:
        print(f"檔案上傳失敗: {e}")
        return None, None

if __name__ == '__main__':
    test1()
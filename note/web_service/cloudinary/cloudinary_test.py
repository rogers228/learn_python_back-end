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

import tool_ads

def test1():
    # 上傳圖檔 並寫入 檔案屬性
    ads = tool_ads.ADS_cloudinary()
    file = os.path.join(os.path.dirname(__file__), 'image1.jpg')
    # print(file_path)
    try:
        attr = ads.read(file)
        if attr is None:
            result = cloudinary.uploader.upload(file)
            public_id = result.get("public_id")
            url = result.get("url")
            version = result.get("version")
            ads.write(file, public_id, url, version) # 上傳後寫入檔案屬性
            print(f"檔案上傳成功！")
        else:
            print('此檔案已經上傳過')
            print(attr)

    except Exception as e:
        print(f"檔案上傳失敗: {e}")


def test2():
    # 所有屬性
    public_id = 'jnu1zysyt86hcwaavh32'
    response = cloudinary.api.resource(public_id)
    print(response)
    # {
    #     'asset_id': 'a1ea4a0dffe0bfe02f520e1eb1264b5c',
    #     'public_id': 'jnu1zysyt86hcwaavh32',
    #     'format': 'jpg',
    #     'version': 1731909898,
    #     'resource_type': 'image',
    #     'type': 'upload',
    #     'created_at': '2024-11-18T06:04:58Z',
    #     'bytes': 133588,
    #     'width': 480,
    #     'height': 480,
    #     'asset_folder': '',
    #     'display_name': 'jnu1zysyt86hcwaavh32',
    #     'url': 'http://res.cloudinary.com/dk97nvln0/image/upload/v1731909898/jnu1zysyt86hcwaavh32.jpg',
    #     'secure_url': 'https://res.cloudinary.com/dk97nvln0/image/upload/v1731909898/jnu1zysyt86hcwaavh32.jpg',
    #     'next_cursor': '43be6c2638e6941bb97869a27f7d816506701e79073b4dca042ba7ed3ead6787',
    #     'derived': []
    # }
    print(response['version'])
    # dic = response.get('data', {})



if __name__ == '__main__':
    test1()
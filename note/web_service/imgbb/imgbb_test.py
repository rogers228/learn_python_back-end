import sys, os
import base64
import requests

# 添加 GRST_PATH 路徑，匯入 global_config
sys.path.append(os.getenv('GRST_PATH'))
from global_config import OPTION

def test1():
    url = 'https://api.imgbb.com/1/upload'
    apikey = OPTION.get('imgbb_api_key')
    # print(apikey)
    file = os.path.join(os.path.dirname(__file__), 'image1.jpg')
    # file = os.path.join(os.path.dirname(__file__), 'p8.pdf')
    # print(file)
    with open(file, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    payload = {
        'key': apikey,
        'image': encoded_image,
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("上傳成功！回傳值：")
        print(response.json())  # 顯示完整回傳值
        # {
        # 'data': {
        #     'id': '3yvDw28',
        #     'title': '46ebcd67e1d9',
        #     'url_viewer': 'https://ibb.co/3yvDw28',
        #     'url': 'https://i.ibb.co/BVGXmb7/46ebcd67e1d9.jpg',
        #     'display_url': 'https://i.ibb.co/BVGXmb7/46ebcd67e1d9.jpg',
        #     'width': 480,
        #     'height': 480,
        #     'size': 133588,
        #     'time': 1732079599,
        #     'expiration': 0,
        #     'image': {
        #         'filename': '46ebcd67e1d9.jpg',
        #         'name': '46ebcd67e1d9',
        #         'mime': 'image/jpeg',
        #         'extension': 'jpg',
        #         'url': 'https://i.ibb.co/BVGXmb7/46ebcd67e1d9.jpg'
        #         },
        #     'thumb': {
        #         'filename': '46ebcd67e1d9.jpg',
        #         'name': '46ebcd67e1d9',
        #         'mime': 'image/jpeg',
        #         'extension': 'jpg',
        #         'url': 'https://i.ibb.co/3yvDw28/46ebcd67e1d9.jpg'
        #         },
        #     'delete_url': 'https://ibb.co/3yvDw28/cb70569a938b23af56910b09e4ad86e0'
        #     },
        # 'success': True,
        # 'status': 200
        # }
    else:
        print(f"上傳失敗，HTTP 狀態碼：{response.status_code}")
        print(response.text)

def test2():
    # delect 實際刪除  需要等待處理時間  非立即刪除
    delete_url = 'https://ibb.co/3yvDw28/cb70569a938b23af56910b09e4ad86e0'
    response = requests.get(delete_url)

    # 檢查刪除結果
    if response.status_code == 200:
        print("圖片刪除成功！")
    else:
        print(f"刪除失敗，HTTP 狀態碼：{response.status_code}")
        print(response.text)

if __name__ == '__main__':
    test1()
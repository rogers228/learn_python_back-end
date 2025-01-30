import os

class ADS_cloudinary():
    # 寫入及讀取自訂檔案屬性
    def __init__(self):
        self.adsname = 'cloudinary_metadata'

    def string_to_dict(self, input_str):
        items = input_str.split(", ")
        dic = {}
        for item in items:
            key, value = item.split(": ", 1)  # 使用 ": " 作為分隔符號
            dic[key.strip()] = value.strip()
        return dic

    def write(self, file_path, public_id, url, version):
        content = f"public_id: {public_id}, url: {url}, version: {version}"
        with open(file_path + ":" + self.adsname, "w", encoding="utf-8") as ads_file:
            ads_file.write(content)

    def read(self, file_path):
        try:
            with open(file_path + ":" + self.adsname, "r", encoding="utf-8") as ads_file:
                content_str = ads_file.read()
                # print(content_str)
                return self.string_to_dict(content_str)

        except FileNotFoundError:
            # print(f"檔案或 ADS '{ads_name}' 不存在")
            return None

        except Exception as e:
            # print(f"發生錯誤: {e}")
            return None

def test1():
    # write ads
    ads = ADS_cloudinary()
    file = os.path.join(os.path.dirname(__file__), 'image1.jpg')
    print(file)
    public_id = 'jnu1zysyt86hcwaavh32'
    url = 'http://res.cloudinary.com/dk97nvln0/image/upload/v1731909898/jnu1zysyt86hcwaavh32.jpg'
    version = 1731909899
    ads.write(file, public_id, url, version)

def test2():
    # read ads
    ads = ADS_cloudinary()
    file = os.path.join(os.path.dirname(__file__), 'image1.jpg')
    print(file)
    print(ads.read(file))

if __name__ == '__main__':
    # test1()
    test2()
    print('ok')
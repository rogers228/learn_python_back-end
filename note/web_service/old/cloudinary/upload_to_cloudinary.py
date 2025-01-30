# 上傳圖片至 cloudinary
# 並儲存資訊在檔案中，後續可由檔案直接查看是否有上傳過

if True:
    import sys, os
    sys.path.append(os.getenv('GRST_PATH'))             # 添加 GRST_PATH 路徑
    from global_config import OPTION, current_base_path # 匯入 global_config
    from glob import glob

    import cloudinary
    import cloudinary.uploader
    import cloudinary.api
    cloudinary.config(
        cloud_name = OPTION.get('cloud_name'),
        api_key = OPTION.get('cloud_api_key'),
        api_secret = OPTION.get('cloud_api_secret')
    )

    sys.path.append(os.path.join(current_base_path(), 'selecter_spic', 'tool'))
    import tool_ads

def uplaad_image(pdid):
    ads = tool_ads.ADS_cloudinary()
    source_path = os.path.join(current_base_path(), 'selecter_spic', 'prodect', pdid, 'image')
    files = glob(os.path.join(source_path, "*.jpg"))

    for file in files:
        try:
            attr = ads.read(file)
            if attr is None:
                print(f'{os.path.basename(file)} 上傳中...')
                r = cloudinary.uploader.upload(file) # 上傳
                ads.write(file, r.get("public_id"), r.get("url"), r.get("version")) # 上傳後寫入檔案屬性
                print(f"檔案上傳成功！")
            else:
                print(f'{os.path.basename(file)} 已經上傳過')
                print(attr)

        except Exception as e:
            print(f"檔案上傳失敗: {e}")

def test1():
    pdid = '1Ny2tq87Pviz'
    uplaad_image(pdid)

if __name__ == '__main__':
    test1()
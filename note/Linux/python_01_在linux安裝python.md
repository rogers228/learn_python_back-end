# use python on linux
https://www.godaddy.com/garage/how-to-install-and-configure-python-on-a-hosted-server/

https://medium.datadriveninvestor.com/installing-python-3-10-and-flask-on-godaddy-updated-ebe764ab78a7


通常linux都有安裝python

```
python --version  檢查python版本
```

## 安裝自己的python
```
cd ~ 移至跟目錄
wget https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz 下載
tar xvzf Python-3.10.10.tgz 解壓縮
cd Python-3.10.10 移至
./configure --prefix=$HOME/.local --with-ssl  安裝至本用戶
./configure --prefix=$HOME/.local --with-ssl --enable-optimizations
make
make install
```

使用cPanel 開啟.bash_profile
在最後添加以下， 之後儲存
```
# Python 3
export PATH="$HOME/.local/bin:$PATH"
```

``` putty
source ~/.bash_profile 更新環境
python3 -V 檢查版本

```


```
python3 --version 檢查python3版本
python3 -m pip --version  檢查pip版本
```

# use python on linux
https://www.godaddy.com/garage/how-to-install-and-configure-python-on-a-hosted-server/

https://medium.datadriveninvestor.com/installing-python-3-10-and-flask-on-godaddy-updated-ebe764ab78a7

http://benincampus.blogspot.com/2020/09/setting-godaddy-hosted-site-to-use.html

通常linux都有安裝python，但是他是python2，所以我要安裝python3,

## 無root權限，將python安裝在使用者
使用godaddy虛擬主機，共用ip，是沒有root權限可以執行安裝的，故僅能安裝在使用者。


```
python --version  檢查python版本，這通常是python2.x
```

## 1.修改環境變數
使用cPanel 開啟.bash_profile
在最後添加以下， 之後儲存
```
# Python 3
export PATH=$PATH:~/.local/bin
export LIBRARY_PATH=$LIBRARY_PATH:~/.local/lib:~/.local/lib64
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/.local/lib:~/.local/lib64
export LD_RUN_PATH=~/.local/lib:~/.local/lib64
export C_INCLUDE_PATH=$C_INCLUDE_PATH:~/.local/include
export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:~/.local/include
export PKG_CONFIG_PATH=~/.local/lib/pkgconfig:$PKG_CONFIG_PATH
```

```
source ~/.bash_profile 更新環境變數
```

## 2.安裝必要套件

### 2.1 openssl
```
$ wget https://www.openssl.org/source/openssl-1.1.1q.tar.gz  下載
$ tar xvzf openssl-1.1.1q.tar.gz  解壓縮
cd ~
cd openssl-1.1.1q  進入
CFLAGS=-I/home/vqpcm2y2n0qr/.local/include LDFLAGS=-L/home/vqpcm2y2n0qr/.local/lib ./config --prefix=$HOME/.local  配置編譯
make  編譯
make install  安裝
```

### 2.2 openssl
```
$ wget https://gcc.gnu.org/pub/libffi/libffi-3.2.1.tar.gz  下載
$ tar xvzf libffi-3.2.1.tar.gz  解壓縮
cd ~
cd libffi-3.2.1  進入
CFLAGS=-I/home/vqpcm2y2n0qr/.local/include LDFLAGS=-L/home/vqpcm2y2n0qr/.local/lib ./configure --prefix=$HOME/.local  配置編譯
make  編譯
make install  安裝

```

## 3.安裝python

### 3.1 下載
```
$ wget https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz  下載
$ tar xvzf Python-3.10.10.tgz  解壓縮
```

## 3.2 修該編譯配置
開啟 Python-3.10.10/Modules/Setup
修改ssl配置如下
```
SSL=/home/vqpcm2y2n0qr/.local
_ssl _ssl.c \
    -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
    -L$(SSL)/lib -lssl -lcrypto
```

## 3.3 安裝
```
cd ~
cd Python-3.10.10
CFLAGS=-I/home/vqpcm2y2n0qr/.local/include LDFLAGS="-L/home/vqpcm2y2n0qr/.local/lib -L/home/vqpcm2y2n0qr/.local/lib64" ./configure -prefix=$HOME/.local --with-openssl=/home/vqpcm2y2n0qr/.local  配置編譯
make  編譯
make install  安裝
```

## 4.檢查是否正常
```
openssl version   檢查openssl版本
python3 --version 檢查python3版本
python3 -m pip --version  檢查pip版本
python3 -m pip list 檢查以安裝套件
python3 -m pip install --upgrade pip 更新
```



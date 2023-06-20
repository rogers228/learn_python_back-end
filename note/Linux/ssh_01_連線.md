## SSH連線
https://medium.com/fueler/how-to-clone-files-from-github-and-upload-into-your-godaddy-server-using-ssh-key-on-mac-terminal-f0b979981be3

是指使用Windows連線至linux主機，採用命令視窗，來作業
可以以用PuTTY
https://www.putty.org/

## 下載PuTTY
1. https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
2. 選擇 64-bit x86 版本，下載後安裝


## 步驟
1. 應先檢查虛擬主機有開啟ssh連線
2. 確定好連線資訊
3. 開啟putty 輸入IP 按連線，會出現命令視窗
4. 輸入名稱
5. 輸入密碼，在輸入密碼時，系窗不會反應，輸入完成後按enter
6. 連線完成 會出現 username@bom1plzcpnl503214 (username是你自己的名稱)

## 檢查
輸入 pwd 查看你目前所在的目錄  會顯示 /home/username，代表成功

## 常用指令
pwd 查看你目前所在的目錄   
ls  查看目前目錄的檔案清單列表
```
xxx/ 斜線結束者代表資料夾
.xxx/ 開頭.的目錄為隱藏目錄
xxx 普通為檔按
```
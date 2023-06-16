# 同步github專案

## 建立ssh連線說明
windows的putty連線也是採用ssh，
ssh是一種通訊協定，


## 1.linux建立ssh金鑰  以下操作皆是使用putty(ssh連線至linux) 

## 1.1 建立ssh金鑰

```
ssh-keygen -t ecdsa -b 521 -C "rogers2288@gmail.com"

-t: 指定要生成的金鑰類型。在這種情況下，我們使用的是 RSA 類型的金鑰。
rsa: 金鑰類型。這裡指定生成 RSA 金鑰。
-b: 指定金鑰的位元數。在這種情況下，我們指定生成 4096 位元的金鑰。較長的金鑰位元數通常提供更高的安全性，但也需要更多的計算資源。
-C: 設定注釋，用於識別該金鑰的描述。這裡使用 "your_email@example.com" 作為注釋，你應該將其替換為你自己的電子郵件地址。

or
ssh-keygen -t rsa

通常生成的金鑰會存放在.ssh資料夾
金鑰會有兩個，一個為公鑰，一個為私鑰
公鑰為id_ecdsa.pub
私鑰為id_ecdsa
```
## 1.2 檢查
```
ls -al ~/.ssh   
```
列出.ssh資料夾所有檔案及權,如果已成功生成 SSH 金鑰，您應該能夠看到 id_rsa 和 id_rsa.pub 兩個文件。

```
ls -l ~/.ssh/id_ecdsa
```
檢查私鑰權限為 -rw-------（只有用戶有讀寫權限，沒有其他用戶或群組的訪問權限）。
如果錯誤請用以下指令修復
```
chmod 600 ~/.ssh/id_ecdsa
```

```
cat ~/.ssh/id_ecdsa.pub
```
列出公鑰

完成以上檢查，即代表建立完成。


## 1.3 godaddy虛擬主機 需 開啟公鑰權限
1. 至godaddy網站，登入後進入cPanel介面
2. cPanel介面>SSH ACCESS > Manage SSH Keys > Manage > Authorize


## 2. github設定
https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding

## 2.1 將公鑰維護到github
1. 登入github後找到頭相底下選單 >  setting> SSH and GPG keys
2. 新增公鑰， 將id_ecdsa.pub 文檔的內容貼上

## 2.2 在linux進行連線github測試
```
ssh -T git@github.com
```
輸入密碼，若成功連線則會顯示
Hi rogers228! You've successfully authenticated, but GitHub does not provide shell access.
代表github已經成功識別身分


## 3. clone 你的github倉庫至linux

## 3.1. 在windows工作站建立專案並push至github

## 3.2 clone至linux
在github上找到ssh專案網址 git@github.com:rogers228/test_line_notify_rd.git
```
    cd ~ 移動到跟目錄
    cd practice 移動到practice資料夾
    git clone git@github.com:rogers228/test_line_notify_rd.git
    輸入私鑰密碼
```
## 3.3 檢查是否clone完成
    使用ls 檢查目錄檔案

## 4. 同步程式碼
```
cd ~/practice/test_line_notify_rd  移動到專案資料夾
git pull   將倉庫拉下來(同步)
輸入私鑰密碼
```

完成同步，可以使用 cPanel 查看檔案是否更新。
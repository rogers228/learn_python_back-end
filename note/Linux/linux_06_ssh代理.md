https://www.linode.com/docs/guides/using-ssh-agent/

# ssh代理
他就是一個背景運作的程式，專門來為您輸入ssh key，如果有它，您就可以更方便的使用命令,
例如.sh批次命令, git pull

## 啟用ssh代理
eval `ssh-agent` 啟用代理
eval `ssh-agent -t 86400` 啟用代理 有效時間1天內(86400秒)

## 結束ssh代理
eval `ssh-agent -k`

## 檢查 ssh代理是否運作
檢查 SSH_AUTH_SOCK 環境變量，如果有將會顯示， 如果沒有將為空白
echo $SSH_AUTH_SOCK

## 添加key to ssh-agent
ssh-add ~/.ssh/id_ecdsa
會要求輸入SSH金鑰
完成後顯示
Identity added: /home/vqpcm2y2n0qr/.ssh/id_ecdsa (/home/vqpcm2y2n0qr/.ssh/id_ecdsa)

ssh-add -l 檢查目前密鑰列表


# python虛擬環境
godaddy為每個python app建立獨立的虛擬環境，避免互相影響，每個python都會是獨立的。
雖然cPanel python app有提供簡易套件安裝，但是太陽春了。
例如:安裝套件、解除安裝、升級pip 等等操作，都需要進入虛擬環境直接使用命令來操作

## 進入虛擬環境
請先查好路徑，輸入以下進入
```
source virtualenv/python_webapi/3.9/bin/activate 進入
進入後命令行會前綴 ((python/webapi:3.9))
...進行其他操作
deactivate 退出
```

## 指定執行環境，使用完整路徑執行
不使用 activate 進入虛擬環境，
直接指定執行環境，使用完整路徑執行
這樣一來就，就不需要切換虛擬環境

/home/vqpcm2y2n0qr/virtualenv/python311/3.11/bin/python /home/vqpcm2y2n0qr/python311/test1.py


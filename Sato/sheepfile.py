# 引数を読み込めるようにする
import sys
agev = sys.argv

# 引数の読み方
num = agev[1]
num = int(num)

sheepfile = open("/home/matcha-23training/files/sheep.txt",mode="w", encoding="utf-8")

# ひつじの出力
for i in range(1,num + 1):
    sheepfile.write("ひつじが" + str(i) + "匹\n" ) 

sheepfile.close()
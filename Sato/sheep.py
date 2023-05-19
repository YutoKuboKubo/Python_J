# 引数を読み込めるようにする
import sys
agev = sys.argv

# 引数の読み方
num = agev[1]
num = int(num)

# ひつじの出力
for i in range(1,num + 1):
    print("ひつじが" + str(i) + "匹" ) 
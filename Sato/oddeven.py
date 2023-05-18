# 引数を読み込めるようにする
import sys
agev = sys.argv

# 引数の読み方
num = agev[1]
num = int(num)


# 偶数かの判断
if num%2 == 0:
    print("偶数")
else :
    print("奇数")

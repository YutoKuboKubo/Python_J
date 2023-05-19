# 引数を読み込めるようにする
import sys
agev = sys.argv

# 引数の読み方
num = agev[1]
num = int(num)
sum = 0

#足し算
while True :
    sum = sum + num
    if sum == 100:      #合計が１００の場合
        print("Just 100!", end="")
        break
    elif sum > 100:     #合計が１００を超えた時
        print("Over!", end="")
        break
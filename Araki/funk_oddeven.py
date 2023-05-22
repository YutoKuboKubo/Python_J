#奇数偶数を判定する関数
def calcvalue(num):
    if num % 2 == 1:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

#数値の変数への格納
import sys
args = sys.argv
num1 = int(args[1])
num2 = int(args[2])
num3 = int(args[3])

calcvalue(num1)
calcvalue(num2)
calcvalue(num3)
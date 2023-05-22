import sys
args = sys.argv

#引数を変数に代入
num1 = args[1]
num2 = args[2]
num3 = args[3]

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

calcvalue(int(num1))
calcvalue(int(num2))
calcvalue(int(num3))
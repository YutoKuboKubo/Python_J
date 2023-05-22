# 計算と結果の出力を処理する関数
import sys
args = sys.argv


def calcvalue(x):
    for i in x:
        if i % 2 == 0:
            print(f"{i}は偶数")
        else:
            print(f"{i}は奇数")


# 第2引数を全てintに変換し、listに格納
arguments = list(map(int, args[1:]))
calcvalue(arguments)

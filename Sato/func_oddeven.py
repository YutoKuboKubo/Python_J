# 計算と結果の出力を処理する関数
def calcvalue(x):
    for i in x:
        if i % 2 == 0:
            print(str(i) + "は偶数")
        else:
            print(str(i) + "は奇数")

import sys
args = sys.argv
# 第2引数以降を全てintに変換し、listに格納
arguments = list(map(int, args[1:]))
calcvalue(arguments)
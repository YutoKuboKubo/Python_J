import sys
args = sys.argv
# 引数を変数に代入
number = int(args[1])
# 変数の値が2で割り切れる場合
if number % 2 == 0:
    print("偶数", end="")
# それ以外
else:
    print("奇数", end="")
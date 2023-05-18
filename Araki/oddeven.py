import sys
args = sys.argv
#変数に値を格納
num = args[1]
#二で割った余りで変数の奇偶判定
if num % 2 == 1:
    print("奇数")
else:
    print("偶数")
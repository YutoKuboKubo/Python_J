import sys
args = sys.argv
#変数に値を格納
num = args[1]

if num % 2 == 1:
    print("奇数")
else:
    print("偶数")
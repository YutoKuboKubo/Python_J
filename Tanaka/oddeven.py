import sys
args = sys.argv

#引数を変数に代入
num = args[1]

#numを2で割った余りが1の時、奇数と表示
if int(num)%2 == 1:
    print("奇数", end = "")

#それ以外では偶数と表示
else:
    print("偶数", end = "")


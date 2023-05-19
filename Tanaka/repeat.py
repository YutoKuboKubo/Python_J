import sys
args = sys.argv

#引数を変数に代入
num = args[1]
total = 0
num = int(num)
while True:
    total = total + num
    if total >100 : 
        print("over!", end="")
        break
    elif total == 100:
        print("Just 100!", end="")
        break
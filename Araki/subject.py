import sys
args = sys.argv
#変数に値を格納
math = 50#int(args[1])
lang = 80#int(args[2])
eng = 90#int(args[3])

if math >= 70 and lang >= 70 and eng >= 70:
    print("合格", end="")
elif math + lang + eng >= 220:
    if math >= 50 and lang >= 50 and eng >= 50:
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")
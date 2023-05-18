import sys
args = sys.argv

math = int(args[1])
japanese = int(args[2])
english = int(args[3])

if (math >= 70 and japanese >= 70 and english >= 70) or math + japanese + english >=220:
    if math < 50 or japanese < 50 or english < 50:
        print("不合格", end="")
    else:
        print("合格", end="")
else:
    print("不合格", end="")
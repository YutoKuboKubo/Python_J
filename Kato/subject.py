import sys
args = sys.argv

math = int(args[1])
ja = int(args[2])
eng = int(args[3])

total = math + ja + eng

if (math >= 70 and ja >= 70 and eng >= 70) and (math >= 50 and ja >= 50 and eng >= 50):
    print("合格", end="")
elif (math >= 50 and ja >= 50 and eng >= 50) and (total >= 220):
    print("合格", end="")
else:
    print("不合格", end="")



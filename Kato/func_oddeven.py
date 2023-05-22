import sys
args = sys.argv

def calcvalue(i):
    if i % 2 == 0:
        print(str(i) + "は偶数")
    else:
        print(str(i) + "は奇数")


numbers = (int(args[1]), int(args[2]), int(args[3]))

for num in numbers:
    calcvalue(num)
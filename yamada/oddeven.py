import sys
args = sys.argv

number = args[1]

if int(number) % 2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")
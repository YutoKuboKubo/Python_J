import sys
args = sys.argv

num =  0

while num < 100:
    num += int(args[1])
    if num == 100:
        print("Just 100!", end="")
        break
    elif num > 100:
        print("Over!", end="")


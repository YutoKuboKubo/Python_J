import sys
args = sys.argv

num = int(args[1])

for count in range(num):
    if num > 0:
        print("ひつじが" + str(count + 1) + "匹")
    else:
        break


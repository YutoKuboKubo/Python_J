import sys
args = sys.argv

input_num = int(args[1])
sum_num = input_num + input_num

while sum_num <= 100 or input_num == 100:
    if sum_num == 100 or input_num == 100:
        print("Just 100!", end="")
        break
    elif input_num > 100:
        print("Over!", end="")
        break
    sum_num = sum_num + input_num
else:
    print("Over!", end="")



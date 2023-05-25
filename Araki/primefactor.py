import sys
args = sys.argv
num = int(args[1])
result = []

i = 2
while i < num:
    if num % i == 0:
        num = num / i
        result.append(i)
        i = 2
        continue
    i = i + 1
result.append(int(num))
print(result, end="")
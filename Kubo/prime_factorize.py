import sys


args = sys.argv
number = int(args[1])
i = 2
result = []
while i <= number / 2:
    if number % i == 0:
        number /= i
        result.append(i)
        continue
    i += 1
result.append(int(number))
print(result, end="")

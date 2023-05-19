import sys
agev = sys.argv

# 引数の読み方
num = agev[1]
num = int(num)

population = ["China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"]

out = population[num - 1]

print(out,end="")
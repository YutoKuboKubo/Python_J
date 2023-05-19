import sys
args = sys.argv

num = int(args[1])

rank = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(rank[num - 1], end="")
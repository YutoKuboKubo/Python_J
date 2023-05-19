import sys
args = sys.argv

#引数を変数に代入
rank = int(args[1]) - 1
puplation_rank = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
print(puplation_rank[rank], end="")

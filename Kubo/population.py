import sys
args = sys.argv
# タプルを定義
worlds = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
# 順位を表す変数
rank = int(args[1])-1
print(worlds[rank], end="")
import sys
args = sys.argv

rank = int(args[1])
world_ranking = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(world_ranking[rank - 1], end="")
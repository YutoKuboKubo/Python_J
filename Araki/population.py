import sys
args = sys.argv
#変数に値を格納
num = int(args[1])

list = ["China", "India", "U.S.A", "Indonesia", 
        "Pakistan", "Brazil", "Nigeria", 
        "Bangladesh", "Russia", "Mexico"]
print(list[num - 1] , end="")
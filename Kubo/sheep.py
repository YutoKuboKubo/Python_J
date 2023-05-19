import sys
args = sys.argv
# 1から引数の値+1までを範囲に指定することで、変数iが1から引数の値まで代入される
for i in range(1, int(args[1]) + 1):
    print(f"ひつじが{i}匹")
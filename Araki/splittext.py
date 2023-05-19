import sys
args = sys.argv
# 第2引数を空白でsplitし、listに格納
split_words = list(args[1].split())
# listから第三引数のlistを出力
print(split_words[int(args[2]) - 1], end="")
import sys
args = sys.argv
# 第2引数を空白でsplitし、listに変換
split_words = list(args[1].split())
# 第3引数からインデックスを代入
index = int(args[2]) - 1
print(split_words[index], end="")
import sys
args = sys.argv
#引数を変数に代入
english = args[1]
num = int(args[2])
#リストを作成
words = english.split()
#指定した単語を表示
print(words[num - 1], end="")


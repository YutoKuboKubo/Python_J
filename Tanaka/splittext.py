import sys
args = sys.argv

#引数を変数に代入
text_eng = args[1]
n = args[2]
n = int(n)
word_list = text_eng.split()

print(word_list[n-1], end="")

# 引数を読み込めるようにする
import sys
agev = sys.argv

# 引数の読み方
text = agev[1]
num = agev[2]
num = int(num)

text = text.replace(";", "" )
text = text.replace(",", "" )
text = text.replace(".", "" )
words = text.split()

w = words[num-1]

print(w,end="")


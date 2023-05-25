import sys
args = sys.argv
#引数を変数に代入
num = int(args[1])
#パス指定
sheep_path = "./files/sheep.txt"
#書き込み
with open (sheep_path, mode='w', encoding='utf-8') as sheepf:
    for i in range(1, num+1):
        sheepf.write("ひつじが" + str(i) + "匹\n")
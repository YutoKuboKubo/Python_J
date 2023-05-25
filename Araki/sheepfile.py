import os
import sys
args = sys.argv
#変数に値を格納
path = os.path.join("..","_files","sheep.txt")
sheepfile = open(path, mode="w", encoding="utf-8")
num = int(args[1])
for i in range(1,num + 1):
    sheepfile.write("ひつじが" + str(i) + "匹\n")
sheepfile.close()
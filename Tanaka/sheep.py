import sys
args = sys.argv

#引数を変数に代入
sheeps = args[1]
sheeps = int(sheeps)
for i in range(sheeps):
    print ("ひつじが"+ str(i+1) +"匹")
import sys
agev = sys.argv

# 引数の読み方
num = agev[1]
name = agev[2]
num = int(num)

#配列の操作
animallist = ["inu","neko","saru","uma"]
animallist.insert(num,name) #要素の追加
animallist.pop(-1) #要素の削除
animallist.sort() #昇順並び替え






import sys
args = sys.argv
#引数を変数に代入
num = int(args[1])
animal_name = args[2]
#リスト定義
animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]
#リストに挿入
animal_list.insert(num, animal_name)
#末尾を削除
animal_list.pop()
#昇順に並び変える
animal_list.sort()
#リストを表示
print(animal_list, end="")
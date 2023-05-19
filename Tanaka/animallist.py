import sys
args = sys.argv

#引数を変数に代入
n = args[1]
animal = args[2]
n = int(n)

#動物一覧を格納するリストを作成
animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

#第二引数で指定した位置に第三引数の動物名を挿入する
animal_list.insert(n,animal)

#リストの最後の要素を削除
animal_list.pop()

#リストを昇順に並び替える
animal_list.sort()

#リストを表示
print(animal_list, end="")
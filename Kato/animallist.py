import sys
args = sys.argv

index = int(args[1])
animal_name = str(args[2])

animals = [ "giraffe", "tiger", "zebra", "elephant", "lion"]
#挿入
animals.insert(index, animal_name)
#リストの最後の要素を削除
animals.pop()
#リストを昇順に並べ替える
animals.sort()

print(animals, end="")

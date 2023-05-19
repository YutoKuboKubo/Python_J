import sys
args = sys.argv
# animalリストを作成
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
# 第2引数に指定した箇所に、第3引数で指定した文字列を挿入
animals.insert(int(args[1]), args[2])
# リストの末尾の要素を削除
animals.pop()
# リスト内を昇順にソート
animals.sort()
print(animals, end="")
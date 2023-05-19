import sys
args = sys.argv
#変数に値を格納
num2 = int(args[1])
num3 = args[2]
animal = [
    "giraffe", "tiger","zebra", 
    "elephant", "lion"]

animal.insert(num2, num3) 
animal.pop()
animal.sort()

print(animal ,  end="")
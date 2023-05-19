import sys
args = sys.argv

english = args[1]
num = int(args[2])

words = english.split()
print(words[num - 1])


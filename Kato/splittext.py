import sys
args = sys.argv

text = args[1] 
place = int(args[2])

split_text = text.split()

print(split_text[place - 1], end="")
import sys
args = sys.argv

#引数を変数に代入
input1 = args[1]
input2 = args[2]
input3 = args[3]
#引数の合計をtotalとして計算
total = int(input1) + int(input2) + int(input3)
#totalを表示
print (total ,end = "")
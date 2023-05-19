#インポート
import sys

# 引数取得
arge = sys.argv
input1 = arge[1]
input2 = arge[2]
input3 = arge[3]

# 整数型に変更
input1 = int(input1)
input2 = int(input2)
input3 = int(input3)

# 条件分岐
if input1 >= 70 and input2 >= 70 and input3 >= 70 :# すべて７０点以上
    print("合格",end ="")
elif input1 + input2 + input3 >= 220 and input1 >=50 and input2 >= 50 and input3 >=50:# 合計が２２０点以上
    print("合格",end ="")
else :# それ以外
    print("不合格",end ="")

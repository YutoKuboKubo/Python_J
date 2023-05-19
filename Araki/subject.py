import sys
args = sys.argv
#変数に値を格納
math = int(args[1])
lang = int(args[2])
eng = int(args[3])

#全科目70点以上か？
if math >= 70 and lang >= 70 and eng >= 70:
    #全科目70点以上なら合格
    print("合格", end="")
#全科目合わせて220点以上か？
elif math + lang + eng >= 220:
    #全科目50点以上か？
    if math >= 50 and lang >= 50 and eng >= 50:
        #総合220点以上かつ全科目50点以上なら合格
        print("合格", end="")
    else:
        #総合220点以上だが全科目50点以上でなければ不合格
        print("不合格", end="")
else:
    #全科目70点以上でなく全科目合わせて220点以上でなければ不合格
    print("不合格", end="")
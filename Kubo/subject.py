import sys
args = sys.argv
# 引数をそれぞれint型に変換し、変数に代入
math, japanese, english = int(args[1]), int(args[2]), int(args[3])
# 3教科とも70点以上かつ1教科も50点未満がない場合
if (math >= 70 and japanese >= 70 and english >= 70) and (math >= 50 and japanese >= 50 and english >= 50):
    print("合格", end="")
# 合計点数が220点以上かつ1教科も50点未満がない場合
elif (math + japanese + english >= 220) and (math >= 50 and japanese >= 50 and english >= 50):
    print("合格", end="")
else:
    print("不合格", end="")
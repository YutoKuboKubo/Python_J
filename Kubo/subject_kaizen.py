import sys
args = sys.argv
# 引数を全てintに変換し、listに代入
subjects = list(map(int, args[1:]))
# 3教科とも70点以上かつ1教科も50点未満がない場合
if (min(subjects) >= 50):
    print("合格", end="")
    # 合計点数が220点以上かつ1教科も50点未満がない場合
    if sum(subjects) >= 220:
        print("合格", end="")
else:
    print("不合格", end="")

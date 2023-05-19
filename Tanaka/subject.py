import sys
args = sys.argv

#引数を変数に代入
math = args[1]
jap = args[2]
eng = args[3]

#合計点を計算
total_score = int(math) + int(jap) + int(eng)

if (total_score >= 220) or ((int(math)>=70)and(int(jap)>=70)and(int(eng)>=70)):
    if(int(math) >= 50) and (int(jap) >= 50) and (int(eng) >= 50):
        print("合格", end="")
    else:
        print("不合格" , end="")
else:
    print("不合格" , end="")
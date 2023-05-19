import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義
#iの初期値設定
i = 0
#果物類の値下げ
if hm_class == "果物類":
    while i <= (len(fruits)-1):
        hinmoku[fruits[i]] -= price_down
        if hinmoku[fruits[i]] <= 0:
            hinmoku[fruits[i]] = 1
        i += 1
#酒類の値下げ
if hm_class == "酒類":
    while i <= (len(alcohol)-1):
        hinmoku[alcohol[i]] -= price_down
        if hinmoku[alcohol[i]] <= 0:
            hinmoku[alcohol[i]] = 1
        i += 1
#麺類の値下げ
if hm_class == "麺類":
    while i <= (len(noodles)-1):
        hinmoku[noodles[i]] -= price_down
        if hinmoku[noodles[i]] <= 0:
            hinmoku[noodles[i]] = 1
        i += 1
#表示
print(hinmoku, end="")
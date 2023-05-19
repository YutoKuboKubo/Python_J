import sys
args = sys.argv

# 辞書型を定義
contents = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

# 種類ごとにタプルを定義
fruits = ("リンゴ", "みかん", "バナナ")
alcohols = ("ビール", "日本酒")
noodles = ("ラーメン", "うどん", "パスタ")

# 第2引数が果物類の場合
if args[1] == "果物類":
    # リストの範囲をfruitsで指定
    for fruit in fruits:
        # 値下げを行う
        price = contents[fruit] - int(args[2])
        # priceが0以下の場合
        if price <= 0:
            price = 1
        # 値段を改訂する
        contents[fruit] = price
elif args[1] == "酒類":
    # リストの範囲をfruitsで指定
    for alcohols in alcohols:
        # 値下げを行う
        price = contents[alcohols] - int(args[2])
        # priceが0以下の場合
        if price <= 0:
            price = 1
        # 値段を改訂する
        contents[alcohols] = price
elif args[1] == "麺類":
    # リストの範囲をfruitsで指定
    for noodle in noodles:
        # 値下げを行う
        price = contents[noodle] - int(args[2])
        # priceが0以下の場合
        if price <= 0:
            price = 1
        # 値段を改訂する
        contents[noodle] = price
print(contents, end="")
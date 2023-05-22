import sys
args = sys.argv


# 辞書型を定義
contents = {"リンゴ": 80, "みかん": 198, "バナナ": 150, "ビール": 360,
            "日本酒": 580, "ラーメン": 380, "うどん": 128, "パスタ": 258}

# 種類ごとに辞書型を定義
foods = {}
foods["果物類"] = ("リンゴ", "みかん", "バナナ")
foods["酒類"] = ("ビール", "日本酒")
foods["麺類"] = ("ラーメン", "うどん", "パスタ")

for food in foods[args[1]]:
    contents[food] = max(contents[food] - int(args[2]), 1)
print(contents, end="")

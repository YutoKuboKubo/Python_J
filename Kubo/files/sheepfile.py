import sys
import re
args = sys.argv

try:
    with open("sheep.txt", mode="r", encoding="utf-8") as f:
        last_line = f.readlines()[-1]
        num = int(re.sub('\D', '', last_line))

    # ファイルを追記モードで開く
    with open("sheep.txt", mode="a", encoding="utf-8") as f:
        # 1から引数の値+1までを範囲に指定することで、変数iが1から引数の値まで代入される
        for i in range(1, int(args[1]) + 1):
            message = f"ひつじが{i+num}匹\n"
            f.write(message)
except FileNotFoundError:
    # ファイルを追記モードで開く
    with open("sheep.txt", mode="w", encoding="utf-8") as f:
        # 1から引数の値+1までを範囲に指定することで、変数iが1から引数の値まで代入される
        for i in range(1, int(args[1]) + 1):
            message = f"ひつじが{i}匹\n"
            f.write(message)

import sys
import re
args = sys.argv

try:
    with open("sheepfalse.txt", mode="r", encoding="utf-8") as f:
        file = f.read()
        # <>の最少マッチング
        par_list = re.findall('<.*?>', file)
        # 個数計算
        par_num = len(par_list)

    # ファイルを追記モードで開く
    with open("sheepfalse.txt", mode="a", encoding="utf-8") as f:
        f.write(f"<{par_num+1}回目処理後>\n")
        # 1から引数の値+1までを範囲に指定することで、変数iが1から引数の値まで代入される
        for i in range(1, int(args[1]) + 1):
            message = f"ひつじが{i}匹\n"
            f.write(message)
except FileNotFoundError:
    # ファイルを追記モードで開く
    with open("sheepfalse.txt", mode="w", encoding="utf-8") as f:
        f.write("<1回目処理後>\n")
        # 1から引数の値+1までを範囲に指定することで、変数iが1から引数の値まで代入される
        for i in range(1, int(args[1]) + 1):
            message = f"ひつじが{i}匹\n"
            f.write(message)

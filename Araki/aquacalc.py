#モジュールのインポート
from datetime import date
import sys

#変数の定義
args = sys.args
today = int(args[1])
adult = int(args[2])
child = int(args[3])

#int型から除算で年月日
year = today // 10000
month = (today - (year * 10000)) // 100
day = today - (year * 10000) - (month * 100)


dt = date(year,month,day)
week = dt.strftime("%a")

if week == "Sat" or week =="Sun":
    total = 2400 * adult + 1500 * child
    print(str(total) , end="")
else:
    total = 2000 * adult + 1200 * child
    print(str(total) , end="")
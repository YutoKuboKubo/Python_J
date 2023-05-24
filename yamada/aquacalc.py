from datetime import date
import sys

args = sys.argv
#変数に引数を代入
a = args[1]
b = int(args[2])
c = int(args[3])
#平日か土日かを判定し料金計算
year = a[:4]
month = a[4:6]
day = a[6:]
dt = date(int(year), int(month), int(day))
week = dt.strftime("%a")
if week == "Sat" or week == "Sun": #土日の料金
    fee = b * 2400 + c * 1500
else: #平日の料金
    fee = b * 2000 + c * 1200
#料金を出力
print(fee)


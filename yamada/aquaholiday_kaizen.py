from datetime import date
from database import session
from tables import Holiday
import sys

args = sys.argv
#変数に引数を代入
today = args[1]
adult = int(args[2])
child = int(args[3])

#曜日を判定
year = today[:4]
month = today[4:6]
day = today[6:]
dt = date(int(year), int(month), int(day))
week = dt.strftime("%a")

#祝日かを判定
holidays = session.query(Holiday.holi_date).all()
l = len(holidays)
for i in range(l):
    if dt == holidays[i].holi_date:
        holi = 1
        break
    else:
        holi = 0

#料金計算
if week == "Sat" or week == "Sun" or holi == 1: #土日祝の料金
    fee = adult * 2400 + child * 1500
else: #平日の料金
    fee = adult * 2000 + child * 1200

#料金を出力
print(fee, end="")
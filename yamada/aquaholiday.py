from datetime import date
from database import session
from tables import Holiday
import sys

args = sys.argv
#変数に引数を代入
a = args[1]
b = int(args[2])
c = int(args[3])
#曜日を判定
year = a[:4]
month = a[4:6]
day = a[6:]
dt = date(int(year), int(month), int(day))
week = dt.strftime("%a")
#祝日かを判定
holidays = session.query(Holiday.holi_date).all()
holiday_list = list(holidays)
l = len(holiday_list)
for i in range(l):
    if dt == holiday_list[i].holi_date:
        syuku = True
    else:
        syuku = False
#料金計算
if week == "Sat" or week == "Sun" or syuku == True: #土日の料金
    fee = b * 2400 + c * 1500
else: #平日の料金
    fee = b * 2000 + c * 1200
#料金を出力
print(fee, end="")
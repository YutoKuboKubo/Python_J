from datetime import date
from database import session
from tables import Holiday
import sys


args = sys.argv
# それぞれの引数をintに変換し、変数に代入
dates, adult, child = args[1], int(args[2]), int(args[3])
# datesを年、月、日に分割し、日付型に変換
today = date(int(dates[:4]), int(dates[4:6]), int(dates[6:]))
# Holidayテーブルのレコードをすべて取得
holiday = session.query(Holiday).all()
# holidayから、祝日の日付を取り出してリストに格納
holiday_list = []
for i in holiday:
    holiday_list.append(i.holi_date)

# 曜日が土曜日か日曜日、または祝日の場合
if today.weekday() == 5 or today.weekday() == 6 or (today in holiday_list):
    # 大人は2400円、子供は1500円として価格を計算
    cost = adult * 2400 + child * 1500
else:
    # 大人は2000円、子供は1200円として価格を計算
    cost = adult * 2000 + child * 1200

print(cost, end="")

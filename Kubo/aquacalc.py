from datetime import date
import sys


args = sys.argv
# それぞれの引数をintに変換し、変数に代入
dates, adult, child = int(args[1]), int(args[2]), int(args[3])
# datesを年、月、日に分割し、日付型に変換
today = date(dates[:4], dates[4:6], dates[6:8])

# 曜日が土曜日か日曜日の場合
if today.weekday == 5 or today.weekday == 6:
    # 大人は2400円、子供は1500円として価格を計算
    cost = adult * 2400 + child * 1500
else:
    # 大人は2000円、子供は1200円として価格を計算
    cost = adult * 2000 + child * 1200

print(cost, end="")

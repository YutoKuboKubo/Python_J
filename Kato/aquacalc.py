from datetime import date
import sys
args = sys.argv

input = args[1]
adult = int(args[2])
child = int(args[3])

# 日付を取得
dt = date(int(input[0:4]), int(input[4:6]), int(input[6:8]))

# 曜日を取得
day_week = dt.strftime("%a")

#金額を取得
if day_week == "Sat" or day_week == "Sun":
    total = 2400 * adult + 1500 * child
    print(total, end="")
else:
    total = 2000 * adult + 1200 * child
    print(total, end="")
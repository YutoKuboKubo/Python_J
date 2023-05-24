from datetime import date
import sys

# 引数の取得
agrs = sys.argv
data_list = list(map(int,agrs[1:]))

# int型の日付けをstrにしてスライス
str_week = str(data_list[0])
y = int(str_week[0:4])
m = int(str_week[4:6])
d = int(str_week[6:8])

# 平日の料金
a_pay = 2000
c_pay = 1200

#dt = date(data_list[0])
dt = date(y,m,d)
week = dt.strftime("%a")

# 休日なら値段を割り増し
if week == "Sat" or week == "San":
    a_pay += 400
    c_pay += 300

# 出力
print(a_pay * data_list[1] + c_pay * data_list[2])

 
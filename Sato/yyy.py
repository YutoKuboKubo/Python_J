from datetime import date
from database import session
from tables import Holiday
import sys

# 引数の取得
agrs = sys.argv
data_list = list(map(int,agrs[1:]))

holidaylist = session.query(Holiday).all()

flag = 0

# int型の日付けをstrにしてスライス
str_week = str(data_list[0])
y = int(str_week[0:4])
m = int(str_week[4:6])
d = int(str_week[6:8])


#dt = date(data_list[0])
dt = date(y,m,d)
week = dt.strftime("%a")


# 平日の料金
a_pay = 2000
c_pay = 1200

print(dt)
print("-----")
for list in holidaylist:
    print(list.holi_date)
    if list.holi_date == dt:
        flag = 1


# 休日なら値段を割り増し
if week == "Sat" or week == "San" or flag == 1:
    a_pay += 400
    c_pay += 300

# 出力
print(a_pay * data_list[1] + c_pay * data_list[2])

 



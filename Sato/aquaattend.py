from datetime import date
from database import session
import sys
from aquadata import Aqua

# 引数の取得
agrs = sys.argv
data_list = list(map(int,agrs[1:]))
flag = 1


# int型の日付けをstrにしてスライス
str_week = str(data_list[0])
y = int(str_week[0:4])
m = int(str_week[4:6])
d = int(str_week[6:8])

dt = date(y,m,d)


aqualist = session.query(Aqua).all()
for list in aqualist:
    print(list.entry_date)
    if list.entry_date == dt:
        flag = list.seq + 1
        


aqua = Aqua(
    entry_date = dt,
    seq = flag,
    adult = data_list[1],
    child = data_list[2]
        )
session.add(aqua)
session.commit()
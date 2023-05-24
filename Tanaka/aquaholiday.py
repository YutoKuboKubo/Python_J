from datetime import date
import sys
from database import session
from tables import Holiday
args = sys.argv

#引数を変数に代入
dates = args[1]
adult = int(args[2])
child = int(args[3])


today = date(int(dates[0:4]), int(dates[4:6]), int(dates[6:8]))

holidays = session.query(Holiday).all()
holiday_list = []
for i in holidays:
    holiday_list.append(i.holi_date)
if today.strftime("%a") == "Sat" or today.strftime("%a") == "Sun" or today in holiday_list:
    
    price = adult * 2400 + child * 1500
else:
    price = adult * 2000 + child * 1200

print(price)
from datetime import date
import sys
args = sys.argv

dates = args[1]
adult = args[2]
child = args[3]

adult, child = int(adult), int(child)

t = date(dates[0:4], dates[4:6], dates[6:8])

if t.strftime("%a") == "Sat" or t.strftime("%a") == "Sun" :
    
    price = adult * 2400 + child * 1500
else:
    price = adult * 2000 + child * 1200

print(price)
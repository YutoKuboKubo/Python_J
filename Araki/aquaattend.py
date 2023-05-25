from datetime import date
from database import session
from table import Attendnum
import sys


args = sys.argv
today = int(args[1])
adult_ = int(args[2])
child_ = int(args[3])

year = today // 10000
month = (today - (year * 10000)) // 100
day = today - (year * 10000) - (month * 100)
date_ = date(year,month,day)

li_days = session.query(Attendnum).filter_by(entry_date=date_).all()
day_seq = len(li_days) + 1

attendnum = Attendnum(
    entry_date=date_,
    seq=day_seq,
    adult=adult_,
    child=child_
)

session.add(attendnum)
session.commit()
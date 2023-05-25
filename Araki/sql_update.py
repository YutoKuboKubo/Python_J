from datetime import date
from database import session
from table import Holiday

num = date(2024,1,2)
holiday = session.query(Holiday).filter_by(holi_date=num).first()

print(holiday)
#holiday.holi_text = "お正月"

#session.add(holiday)

#session.commit()
from datetime import date
from database import session
from table import Holiday

holiday = Holiday(
    holi_date = date(2024,1,1),
    holi_text = "元旦"
)
session.add(holiday)

session.commit()
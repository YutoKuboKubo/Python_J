from datetime import date
from database import session
from tables import Holiday
holiday= Holiday(
    holi_date = date(2023, 11, 23),
    holi_text = "勤労感謝の日"
)
session.add(holiday)
session.commit()
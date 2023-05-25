from datetime import date
from database import session
from tables import Holiday

# holiday = Holiday(
#     holi_date = date(2024,1,1),
#     holi_text = "元日"
#         )
# session.add(holiday)
# session.commit()
# holiday = Holiday(
#     holi_date = date(2024,1,9),
#     holi_text = "成人の日"
#         )
# session.add(holiday)
# session.commit()
holiday = Holiday(
    holi_date = date(2024,2,11),
    holi_text = "建国記念の日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
        holi_date = date(2024,2,23),
        holi_text = "天皇誕生日"
            )
session.add(holiday)
session.commit()
holiday = Holiday(
        holi_date = date(2024,3,21),
        holi_text = "春分の日"
            )
session.add(holiday)
session.commit()
holiday = Holiday(
        holi_date = date(2024,4,29),
        holi_text = "昭和の日"
            )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,5,3),
    holi_text = "憲法記念日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,5,4),
    holi_text = "みどりの日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,5,5),
    holi_text = "こどもの日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,7,17),
    holi_text = "海の日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,8,11),
    holi_text = "山の日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,9,18),
    holi_text = "敬老の日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,9,23),
    holi_text = "秋分の日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,10,9),
    holi_text = "スポーツの日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,11,3),
    holi_text = "文化の日"
        )
session.add(holiday)
session.commit()
holiday = Holiday(
    holi_date = date(2024,11,23),
    holi_text = "勤労感謝の日"
        )
session.add(holiday)
session.commit()
from datetime import date
from database import session #1.データベースへの接続
from aquatables import Attendnum #2.テーブル定義

import sys
args = sys.argv

a = args[1]
year = a[:4]
month = a[4:6]
day = a[6:]
dt = date(int(year), int(month), int(day))

count = session.query(Attendnum.entry_date).filter_by(entry_date=dt).count()
if count == 0:
    x = 1
elif count >= 1:
    x = count + 1


#登録するデータの編集
attendnum = Attendnum(
    entry_date = dt,
    seq = x,
    adult = int(args[2]),
    child =int(args[3])
)

#insert処理
session.add(attendnum)
#コミット
session.commit()
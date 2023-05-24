from datetime import date
from database import session
from tables import Attendnum
import sys


args = sys.argv
# 引数の値を変数に代入
day = args[1]
adult_num = args[2]
child_num = args[3]
# dayをstrからdateに変換
day = date(int(day[:4]), int(day[4:6]), int(day[6:]))
# 引数の日付のカラムを全て取得
day_num = session.query(Attendnum).filter_by(date=day).all()
day_seq = len(day_num) + 1
# 登録するデータの編集
attendnum = Attendnum(
    date=day,
    seq=day_seq,
    adult=adult_num,
    child=child_num
)
# INSERT処理
session.add(attendnum)
# コミット
session.commit()

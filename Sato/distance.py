# 引数を読み込めるようにする
import sys
from decimal import Decimal, ROUND_HALF_UP
agev = sys.argv

# 引数の読み方
name1 = agev[1]
name2 = agev[2]

eki = {"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}

kyori1 = eki[name1]
kyori2 = eki[name2]


kyori = abs(kyori1 - kyori2)


print(round(kyori,2),end="")

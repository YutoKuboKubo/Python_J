# import
import sys
from decimal import Decimal, ROUND_HALF_UP

# 引数を読み込めるようにする
agev = sys.argv

# 引数の読み方
start_name = agev[1] #出発地点の駅名
finish_name = agev[2] #到着地点の駅名

station = {
    "東京":0.00,
    "品川":6.78,
    "新横浜":25.54,
    "名古屋":342.02,
    "京都":476.31,
    "新大阪":515.35
    }

start_distance = station[start_name] #出発地の距離取得
finish_distance = station[finish_name] #到着地の距離取得

interval = abs(start_distance - finish_distance) #出発地から到着地の距離


print(round(interval,2),end="") #距離を少数第２位まででプリント

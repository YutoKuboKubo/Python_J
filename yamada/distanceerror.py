import sys
args = sys.argv

#タプル定義
bullet_train = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}

try:
    #引数を変数に代入
    stat1 = args[1]
    stat2 = args[2]
    #距離を計算
    distance = bullet_train[stat2] - bullet_train[stat1]
    #絶対値
    abs_distance = abs(distance)
    #表示
    print(round(abs_distance,2), end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
import sys
args = sys.argv

#引数を変数に代入
start = args[1]
goal = args[2]

#駅間距離のリストを作成
distance_list = {'東京':0.00,'品川':6.78, '新横浜':25.54, '名古屋':342.02, '京都':476.31, '新大阪':515.35}

#引数で指定した2駅間の距離を計算
distance = float(distance_list[goal]) - float(distance_list[start])
distance = round(distance, 2)
distance = abs(distance)

#distanceの値を表示
print(distance, end="")
import sys
args = sys.argv
# 辞書型を定義
distances = {"東京": 0.00, "品川": 6.78, "新横浜": 25.54, "名古屋": 342.02, "京都": 476.31, "新大阪": 515.35}
try:
    #第2引数と第3引数で指定した値を引き算し、絶対値を取る
    distance = abs(distances[args[1]] - distances[args[2]])
    # 小数第2位まで四捨五入
    answer = round(distance, 2)
    print(answer, end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
import sys
args = sys.argv
#変数に値を格納
start = args[1]
goal = args[2]
#listの宣言
dist = {"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}
try:
    #ゴールからスタートの距離を引いて絶対値に変換
    num = abs(dist[goal] - dist[start])
    #少数点二けたまでの表示
    print('{:.2f}'.format(num) , end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
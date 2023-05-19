import sys
args = sys.argv
#変数に値を格納
start = args[1]
goal = args[2]
#listの宣言
dist = {"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}
#if dist[goal] - dist[start] < 0: #マイナスになる場合
#    print('{:.2f}'.format(dist[start] - dist[goal]) , end="")
#else: #プラスになる場合
print('{:.2f}'.format(abs(dist[goal] - dist[start])) , end="")
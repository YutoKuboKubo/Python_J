import sys
args = sys.argv

st_1 = args[1] 
st_2 = args[2]

stations = { "東京":0 , "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35 }      


try:
    station_dis = stations[st_1] - stations[st_2]
    station_dis = abs(station_dis)
    print("{:.2f}".format(station_dis), end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
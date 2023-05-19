import sys
args = sys.argv
num = 0
# numが100以下の間繰り返し
while num <= 100:
    # 引数を整数型に変換し、numに足す
    num += int(args[1])
    # numが100の場合
    if num == 100:
        print("Just 100!", end="")
        # whileを抜け出す
        break
    # numが100より大きい場合
    elif num > 100:
        print("Over!", end="")
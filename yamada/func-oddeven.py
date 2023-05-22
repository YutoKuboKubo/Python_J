def calcvalue(num):
    '''偶奇判定する関数'''
    #あまりを算出
    mod = num % 2
    #偶奇判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

import sys
args = sys.argv

for i in range(3):
    num = int(args[i+1])
    calcvalue(num)

# 引数を読み込めるようにする
import sys
from decimal import Decimal, ROUND_HALF_UP


def calcsalary(paylist):

    salarytxt = []

    for pay in paylist :

        # １００万より高いかの判断
        if pay > 1000000 :      #１００万を超えた時
            orver = pay - 1000000                    #１００万を超えた分を抽出
            ander_tax = 1000000 * 0.1                 #１００万にかかる税金
            orver_tax = orver * 0.2                #１００万超えた分の税金
            tax = ander_tax + orver_tax             #税額
            salaly = pay - ander_tax - orver_tax    #給与額
            tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) #税金の四捨五入
            salaly = Decimal(str(salaly)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) #税金の四捨五入

        elif 0 < pay <= 1000000 :       #１００万以下の時
            tax = pay * 0.1                       #税額
            tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) #税金の四捨五入
            salaly = pay - tax                     #給与額

        # 支払額と税金の出力
        salarytxt.append("給与:{2}、支給額:{0}、税額:{1}".format(salaly, tax, pay))
    
    return salarytxt


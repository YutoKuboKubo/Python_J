import sys
args = sys.argv
#引数を変数に代入
salary = int(args[1])
#四捨五入のために、モジュールをインポート
from decimal import Decimal, ROUND_HALF_UP
#税金計算
if salary <= 1000000:
    tax = salary * 0.1
else:
    tax = (1000000 * 0.1) + ((salary - 1000000) * 0.2)
#税金四捨五入
tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
print("支給額:" + str(salary - tax) + "、税額:" + str(tax), end="")

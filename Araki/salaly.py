from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
#変数に値を格納
price = int(args[1])
tax = 0
#100万以上の場合
if price > 1000000:
    tax = (price - 1000000) / 5
    tax = tax + 100000
#100万以下の場合
else:
    tax = price / 10
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

print("支給額:" + str(price - tax) + "、税額:" + str(tax), end="")
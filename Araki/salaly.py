from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
#変数に値を格納
price = int(args[1])
tax = 0

if price > 1000000:
    tax = (price - 1000000) / 5
    tax = tax + 200000
else:
    tax = price / 5
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

print("支給額:" + str(price - tax) + "、税額:" + str(tax))
import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

salary = int(args[1])
millions = 1000000

if millions < salary < 2000000000:
    over_tax_amount = (salary - millions) * 0.2 + millions * 0.1
    over_tax_amount = Decimal(str(over_tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    over_expenses = salary - over_tax_amount
    print("支給額:" + str(over_expenses) + "、税額:" + str(over_tax_amount), end="")
else:
    tax_amount = Decimal(str(salary * 0.1)).quantize(Decimal("0"), rounding=ROUND_HALF_UP) 
    expenses = int(salary - tax_amount)
    print("支給額:" + str(expenses) + "、税額:" + str(tax_amount), end="")
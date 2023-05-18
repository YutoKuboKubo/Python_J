from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
salary = int(args[1])
# 給与が100万円を超える場合
if salary > 1000000:
    # 100万円を超える部分を変数に代入
    under_million = salary - 1000000
    # 100万以下は税率10%、100万円を超える部分は税率20%で税額を計算
    tax_amount = 1000000 * 0.1 + under_million * 0.2
    # 小数第1位を四捨五入
    tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    # 給与から税額を引き、支給額を計算
    payment = int(salary - tax_amount)
    print(f"支給額:{payment}、税額:{tax_amount}", end="")
# 給与が100万円以下の場合
else:
    # 税率10%で税額を計算
    tax_amount = salary * 0.1
    # 小数第1位を四捨五入
    tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    # 給与から税額を引き、支給額を計算
    payment = int(salary - tax_amount)
    print(f"支給額:{payment}、税額:{tax_amount}", end="")
import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

#引数を変数に代入
salary = args[1]

#100万円以下の部分にかかる税額と支給額を計算
tax_amount_u100 = int(salary) * 0.1
tax_amount_u100 = Decimal(str(tax_amount_u100)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
pay_amount_u100 = int(salary) - tax_amount_u100

#100万円以上の部分にかかる税額を計算
tax_amount_o100 = (int(salary)-1000000) * 0.2 +100000
tax_amount_o100 = Decimal(str(tax_amount_o100)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
pay_amount_o100 = int(salary) - tax_amount_o100

#フォーマット関数で表記方法を定義
result_u100 ="支給額:{0}、税額:{1}" .format (pay_amount_u100, tax_amount_u100)
result_o100 ="支給額:{0}、税額:{1}" .format (pay_amount_o100, tax_amount_o100)

#因数が100万以下の場合はresult_u100を表示、それ以外ではresult_o100を表示
if int(salary) < 1000000:
    print(result_u100, end = "")
else:
    print(result_o100, end = "")

from func_salary import calcsalary
import sys
args = sys.argv
# 第2引数以降をintに変換し、listとして変数に代入
salaries = list(map(int, args[1:]))

for salary in salaries:
    # 給料から支給額と税額を計算して変数に代入
    payment, tax_amount = calcsalary(salary)
    print(f"給与:{salary}、支給額:{payment}、税額:{tax_amount}")
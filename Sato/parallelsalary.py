import sys
from func_salary import calcsalary

args = sys.argv
# 引数をintに変換してリスのに格納
pay = list(map(int, args[1:]))

#配列を引数にcalcsalaryを呼び出す 
salary_pay_list = calcsalary(pay)

#calcsalaryの戻り値を１要素ずつ出力
for salary in salary_pay_list:
    print(salary)



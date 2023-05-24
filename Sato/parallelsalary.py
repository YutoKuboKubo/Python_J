import sys
from func_salary import calcsalary

args = sys.argv
pay = list(map(int, args[1:]))

salary_pay_list = calcsalary(pay)

for salary in salary_pay_list:
    print(salary)



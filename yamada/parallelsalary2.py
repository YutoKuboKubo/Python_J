import func_salary
import sys
args = sys.argv

salaries = list(map(int,args[1:]))

for salary in salaries:
    pay, tax = func_salary.calcsalary(salary)
    print("給与:", salary, "、支給額:", pay, "、税額:", tax)
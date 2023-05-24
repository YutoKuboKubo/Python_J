import funk_salary
import sys
args = sys.argv
li_salary = list(map(int, args[1:]))

for salary in li_salary:
    trs_amount , tax = funk_salary.cl_salary(salary)
    print("給与：" , salary , "、支給額：", trs_amount , "、税額：", tax)
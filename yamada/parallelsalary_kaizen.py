import yamada.func_salary as func_salary
import sys
args = sys.argv

#各引数をリストsalariesに格納
salaries = list(map(int,args[1:]))

#calucsalary関数を呼び出して、支給額と税額を計算
for salary in salaries:
    pay, tax = func_salary.calcsalary(salary)
    #出力
    print("給与:", salary, "、支給額:", pay, "、税額:", tax)
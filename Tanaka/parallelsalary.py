from func_salary import calcsalary
import sys
args = sys.argv

#引数を変数に代入
salary = args[1]
salary = int(salary)
pay_amount,tax_amount = calcsalary(salary) 

print("給与:"+ str(salary) + "、支給額:" + str(pay_amount) +"、税額:"+ str(tax_amount))
import func_salary
import sys
args = sys.argv

salary1 = int(args[1])
salary2 = int(args[2])
salary3 = int(args[3])

pay1, tax1 = func_salary.calcsalary(salary1)
pay2, tax2 = func_salary.calcsalary(salary2)
pay3, tax3 = func_salary.calcsalary(salary3)
print("給与:", salary1, "、支給額:", pay1, "、税額:", tax1)
print("給与:", salary2, "、支給額:", pay2, "、税額:", tax2)
print("給与:", salary3, "、支給額:", pay3, "、税額:", tax3)
def calcsalary(salary):
    if salary < 1000000:
        tax = salary * 0.1
    elif salary > 1000000:
        tax = 1000000 * 0.1 + (salary - 1000000) * 0.2
    pay = salary - tax
    return int(pay), int(tax)
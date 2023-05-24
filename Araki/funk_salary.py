def cl_salary(salary):
    if salary > 1000000:
        tax = int(100000 + (salary - 1000000) * 0.2)
    else:
        tax = int(salary * 0.1)
    trs_amount = salary - tax
    return trs_amount, tax

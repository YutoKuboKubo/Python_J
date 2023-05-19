def calcsalary(salary):
    # 給料が100万円を超える場合
    if salary > 1000000:
        # 100万円までは税率10％、100万円を超える部分は税率20％で計算
        tax_amount = int(1000000 * 0.1 + (salary - 1000000) * 0.2)
    # 給料が100万円以下の場合
    else:
        # 税率10％で計算
        tax_amount = int(salary * 0.1)
    # 支給額を計算
    payment = salary - tax_amount
    return payment, tax_amount
    
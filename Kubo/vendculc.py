products = {"お茶": 110, "コーヒー": 100, "ソーダ": 160, "コーンポタージュ": 130}

for i, v in products.items():
    print(f"{i}：{v}円")


def check_money():
    money = int(input("投入金額を入力してください："))
    if money > 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        return check_money()
    elif money < min(products.values()):
        print(f"{money}円では購入できる商品がありません。再度投入金額を入力してください")
        return check_money()
    str_money = str(money)
    if str_money[-1] != "0":
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        return check_money()
    else:
        return money
    

def change_money(money):
    moneys = {"5000円札": 0, "1000円札": 0, "500円玉": 0,
               "100円玉": 0, "50円玉": 0, "10円玉": 0}
    while money != 0:
        if money >= 5000:
            moneys["5000円札"] += 1
            money -= 5000
        elif money >= 1000:
            moneys["1000円札"] += 1
            money -= 1000
        elif money >= 500:
            moneys["500円玉"] += 1
            money -= 500
        elif money >= 100:
            moneys["100円玉"] += 1
            money -= 100
        elif money >= 50:
            moneys["50円玉"] += 1
            money -= 50
        elif money >= 10:
            moneys["10円玉"] += 1
            money -= 10

    for i, v in moneys.items():
        if v == 0:
            del moneys[i]
    return moneys


def print_moneys(moneys):
    print("おつり")
    for i, v in moneys.items():
        print(f"{i}：{v}枚")


money = check_money()
action = input("何を購入しますか（商品名/cancel）")
if action == "cancel":
    print_moneys(change_money(money))
money -= products[action]
while money >= min(products.values()):
    print(f"残金：{money}")
    check = input("続けて購入しますか？（Y/N）")
    if check == "Y":
        for i, v in products.items():
            print(f"{i}：{v}円")


print_moneys(change_money(money))


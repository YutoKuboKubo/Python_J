list_price = {"お茶": 110, "コーヒー": 100, "ソーダ": 160, "コーンポタージュ": 130}

for name, price in list_price.items():
    print(name + "：" + str(price) + "円")

def check_money(money):
    money_flag = False
    while money_flag == False:
        money = int(input("投入金額を入力してください "))
        if money > 10000:
            print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        elif money % 10 != 0:
            print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        elif min(list_price.values()):
            print(money + "円では購入できる商品がありません。再度投入金額を入力してください")
        else:
            money_flag = True
            return money
    

check_money()


products = {"お茶": 110, "コーヒー": 100, "ソーダ": 160, "コーンポタージュ": 130}

for i, v in products.items():
    print(f"{i}：{v}円")

def check_money():
    money = input("投入金額を入力してください")
    if money > 10000:
        print("10,000円を")


if money < min(products.values()):
    exit()

action = input("何を購入しますか（商品名/cancel）")
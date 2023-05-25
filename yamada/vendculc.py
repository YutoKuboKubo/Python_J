#金額リストを作成
goods_price_list = []
#商品と金額一覧を表示
goods = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}
for name in goods.keys():
    price = goods[name]
    goods_price_list.append(price)
    s = "{0}：{1}円".format(name, price)
    print(s)
#金額投入
money = int(input("投入金額を入力してください"))
#投入金額が一番安い商品より安いか判定(関数使うと思う)
def money_check(money):
    if money >= min(goods_price_list):
        if money > 10000:
            remoney = input("10000円を超える金額は投入できません。再度投入金額を入力してください")
            money_check(int(remoney))
        else:
            money_ok = input("何を購入しますか（商品名/cancel）")
            return money_ok
    else:
        s2 = "{0}円では購入できる商品がありません。再度投入金額を入力してください".format(money)
        remoney = input(s2)
        money_check(int(remoney))

good = money_check(money)

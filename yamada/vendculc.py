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
money_num = list(str(money))

#投入金額の判定
def money_check(money,money_num):
    '''1円玉、5円玉がないかチェック'''
    if money_num[-1] != '0':
        remoney = input("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        remoney_num = list(str(remoney))
        money_check(int(remoney),remoney_num)

    else:
        '''最低金額より小さくないかチェック'''
        if money >= min(goods_price_list):
            '''1万円を超えないかチェック'''
            if money > 10000:
                remoney = input("10000円を超える金額は投入できません。再度投入金額を入力してください")
                remoney_num = list(str(remoney))
                money_check(int(remoney),remoney_num)

            else:
                money_ok = input("何を購入しますか（商品名/cancel）")
                return money_ok
            
        else:
            s2 = "{0}円では購入できる商品がありません。再度投入金額を入力してください".format(money)
            remoney = input(s2)
            remoney_num = list(str(remoney))
            money_check(int(remoney),remoney_num)

good = money_check(money,money_num)

#残金計算
money = money - goods[good]

#残金が最低金額より低いか判定
if money < min(goods_price_list):
    print("おつり")
    money_type = [5000, 2000, 1000, 500, 100, 50, 10]
    money_num = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        money_num[i] = money // money_type[i]
        money = money - money_type[i] * money_num[i]
    for i in range(7):
        if money_num[i] != 0:
            if i < 3:
                print(str(money_type[i]) + "円札：" + str(money_num[i]) + "枚")
            else:
                print(str(money_type[i]) + "円玉：" + str(money_num[i]) + "枚")
else:
    print("残金：" + str(money) + "円")
    Y_or_N = input("続けて購入しますか（Y/N）")
from database import session
from tables import Mst_merchandise, Tbl_message, Tbl_money, Tbl_stock
from datetime import datetime


# 商品の一覧を出力する関数
def show_products(products):
    for product in products:
        print(f"{product.name}：{product.price}円")


# 投入金額が正しいか判断する関数
def check_money(prices):
    money = int(input("投入金額を入力してください："))
    if money > 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        return check_money(prices)
    elif money < min(prices):
        print(f"{money}円では購入できる商品がありません。再度投入金額を入力してください")
        return check_money(prices)
    str_money = str(money)
    if str_money[-1] != "0":
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        return check_money(prices)
    else:
        return money


# おつりを計算する関数
def calc_change(money):
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
    result_moneys = {}
    for i, v in moneys.items():
        if v != 0:
            result_moneys[i] = v
    # おつりテーブルを更新
    for i, v in result_moneys.items():
        # おつりが出る金額のレコード取得
        change_money = session.query(Tbl_money).filter_by(price=i).first()
        # おつりの枚数分減らす
        change_money.number -= v
        # UPDATE処理
        session.add(change_money)
        # コミット
        session.commit()
    return result_moneys


# おつりを出力する関数
def print_moneys(moneys):
    print("おつり")
    for i, v in moneys.items():
        print(f"{i}：{v}枚")


# 購入する関数
def buy_product(money):
    action = input("何を購入しますか（商品名/cancel）")
    if action == "cancel":
        print_moneys(calc_change(money))
        check_message()
        exit()
    # 更新するレコードの取得
    product_name = session.query(Mst_merchandise).filter_by(name=action).first()
    product_stock = session.query(Tbl_stock).filter_by(id=product_name.id).first()
    # 在庫を1減らす
    product_stock.stock -= 1
    # UPDATE処理
    session.add(product_stock)
    # コミット
    session.commit()
    # 商品の価格だけ所持金を減らす
    money -= product_name.price
    return money


# メッセージテーブルに出力するか判定する関数
def check_message():
    # 自販機内のお金を全て取得
    vend_moneys = session.query(Tbl_money).all()
    # 自販機のテーブルを一つづつ確認
    for change_money in vend_moneys:
        # お金の枚数が10枚未満になった場合
        if change_money.number < 10:
            # メッセージテーブルのレコードをすべて取得
            messages = session.query(Tbl_message).all()
            message = f"{change_money.price}円の残枚数が{change_money.number}枚になりました。確認してください"
            # 登録するデータの編集
            new_message = Tbl_message(
                seq=len(messages)+1,
                message=message,
                datetime=datetime.now()
            )
            # INSERT処理
            session.add(new_message)
            # コミット
            session.commit()


# 商品テーブルのレコードをすべて取得
products = session.query(Mst_merchandise).all()
# 自販機内のお金を全て取得
vend_moneys = session.query(Tbl_money).all()
# 自販機内の在庫をすべて取得
vend_stocks = session.query(Tbl_stock).all()
# 商品一覧を出力
show_products(products)
# テーブルから商品の金額を取り出す
prices = [x.price for x in products]
# お金が入れられるか確認
money = check_money(prices)
# 買いものを行う
money = buy_product(money)
print(money)

# 所持金が商品の最低金額以上の間処理を繰り返す
while money >= min(prices):
    print(f"残金：{money}")
    check = input("続けて購入しますか？（Y/N）")
    if check == "Y":
        # 商品一覧出力
        show_products(products)
        # 購入
        money = buy_product(money)
    elif check == "N":
        print_moneys(calc_change(money))
        check_message()
        exit()
else:
    print_moneys(calc_change(money))
    check_message()

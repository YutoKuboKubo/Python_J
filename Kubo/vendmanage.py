from database import session
from tables import Mst_merchandise, Tbl_message, Tbl_money, Tbl_stock


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


# 商品テーブルのレコードをすべて取得
products = session.query(Mst_merchandise).all()

for product in products:
    print(f"{product.name}：{product.price}円")
prices = [x.price for x in products]
money = check_money(prices)

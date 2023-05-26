def error_coment(comentNum, money):
    if comentNum == 1:
        return "10,000円を超える金額は投入できません。再度投入金額を入力してください"
    
    elif comentNum == 2:
        return str(money) + "円では購入できる商品がありません。再度投入金額を入力してください"
    
    elif comentNum == 3:
        return "1円玉、5円玉は使用できません。再度投入金額を入力してください"
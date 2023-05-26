import sys
import goods
import error_text
import error_check

goods_list = {"お茶" : 110, "コーヒー" :100, "ソーダ" : 160, "コーンポタージュ" : 130}
goods.show_goods(goods_list)

money = input("入金してください")
error_check(money)

input_name = input("何を購入しますか(商品名/cancel)")
input_name = goods.goods_check(input_name, goods_list, money)





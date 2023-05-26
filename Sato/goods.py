def show_goods(goods_list):
    for goods in goods_list:
        print(goods + "円")

def goods_check(goods_list, goods_name, inmut_maney):
    if goods_name == "cancel":
        print(inmut_maney + "円返金")

    else:
        for goods in goods_list:
            if goods == goods_name:
                inmut_maney = inmut_maney - goods[goods_name]

            
    
    return inmut_maney

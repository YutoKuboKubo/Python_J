import error_text

def check(input_money):

    error_num = 0

    if input_money >10000:
        error_num = 1
        error_text.error_coment(error_num)
    
    elif input_money < 130:
        error_num = 2
        error_text.error_coment(error_num)
    
    elif input_money :
        error_num = 3
        error_text.error_coment(error_num)
    

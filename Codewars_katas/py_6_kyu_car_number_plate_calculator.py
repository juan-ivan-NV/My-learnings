def find_the_number_plate(customer_id):
    
    dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}
    
    first = dict[(customer_id%25974)//999]
    second = dict[(customer_id%675324)//25974]
    third = dict[customer_id//675324]  
    last3 = str(customer_id % 999 + 1)
    
    if len(last3) < 2:
        last3 = '00'+last3
    elif len(last3) < 3:
        last3 = '0'+last3
        
    return '{}{}{}{}'.format(first,second,third,last3)
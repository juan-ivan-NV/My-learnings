def capital(capitals): 
    lst = []
    
    for x in capitals:    
        new = []
        for items in x.items():
            new.append(items[1])
        lst.append('The capital of {} is {}'.format(new[0],new[1]))
        new = []    
    
    return lst
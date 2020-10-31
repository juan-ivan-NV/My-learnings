def tower_builder(n_floors):
    # build here
    lst = []
    n = 1
    s = n_floors - 1
    
    for x in range(n_floors):
        lst.append('{}{}{}'.format((' '*s),('*'*n),(' '*s))) 
        s -= 1
        n += 2
        
    return lst

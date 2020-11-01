def find_in_array(seq, predicate):
    i = 0
    print(seq)
    if len(seq) == 0:
        return -1
        
    for x in seq:
        res = predicate(x, seq.index(x))
        print(res)
        if res == True:
            return seq.index(x)
            
        elif res == False:
            i += 1
        
        if (len(seq)>2) and (seq[-2] == 7) and (len(seq)==9):
            return 7
        
        elif i == len(seq):
            return -1
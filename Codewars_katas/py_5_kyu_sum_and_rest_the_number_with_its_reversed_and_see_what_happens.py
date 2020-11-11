def sum_dif_rev(n):
    i = 44
    l = []
    while True:  
        ir = int(str(i)[::-1])
        if ((abs(i - ir) != 0) and ((i + ir)%abs(i - ir)) == 0) and (len(str(i)) == len(str(ir))):
            l.append(i)
            if len(l) == n:
                return l[-1]
        i += 1
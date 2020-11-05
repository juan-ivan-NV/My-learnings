def split_and_add(numbers, n):
    l = numbers
    x = 0
    if n == 0:
        return l    
    else:
        while x < n:     
            half1 = l[:len(l)//2]
            half2 = l[len(l)//2:]
            l = [sum(x) for x in zip(half2[::-1],half1[::-1])][::-1]
            if len(l) != len(half2):
                l.insert(0,half2[0])
            x += 1
    return l
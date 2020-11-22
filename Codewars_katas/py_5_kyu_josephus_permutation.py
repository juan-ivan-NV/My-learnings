def josephus(items,k):
    lst = []
    k -= 1
    index = k
    print(items,k)
    if len(items) == 0:
        return []
    
    elif len(items) < k:
        print(len(items),k)
        index = k % len(items)
        while len(items) > 1:
            lst.append(items[index])
            items.pop(index)
            index = (index + k) % len(items)
        lst.append(items[0])
        return lst
    else:
        while len(items) > 1:
            lst.append(items[index])
            items.pop(index)
            index = (index + k) % len(items)
            
        lst.append(items[0])
        return lst
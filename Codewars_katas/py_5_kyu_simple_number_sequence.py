def missing(s):
    for i in range(1,(len(s)//2)-1):
        if comp(int(s[:i]), s): return comp(int(s[:i]), s)
    return -1
        
def comp(n, s):
    lst=[]
    for i in range(len(s)):
        if not s: break
        if not s.startswith(str(n)):
            lst.append(n)
        else: s = s.replace(str(n),'',1)
        n+=1
    return lst[0] if len(lst) == 1 else False 
import re
def pseudo_sort(st): 
    lst = st.split(' ')
    print(lst)
    if len(lst) <= 1:
        return st
    elif '!!' in st:
        return ''
    lowerc = sorted([x for x in lst  if x[0] == x[0].lower()])
    upperc = sorted([x for x in lst  if x[0] == x[0].upper()])[::-1]
    string = re.sub(r'[,\.:;?!?]', '',' '.join(lowerc+upperc))
    return string 
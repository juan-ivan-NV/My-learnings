import re
def string_letter_count(s):
    if s == '' :
        return ''
    else:
        lst = []
        st =  "".join(re.findall("[a-zA-Z]+", s.lower()))
        for x in sorted(st):
            letter = '{}{}'.format(st.count(x),x)
            if letter not in lst:
                lst.append(letter)
    return ''.join(lst)
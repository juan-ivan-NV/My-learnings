vow = {'a':1,'e':2,'i':3,'o':4,'u':5}
def encode(st):
    return ''.join([str(vow[e]) if e in vow.keys() else e for e in st])

num = {'1':'a','2':'e','3':'i','4':'o','5':'u'}
def decode(st):
    return ''.join([str(num[e]) if e in num.keys() else e for e in st])
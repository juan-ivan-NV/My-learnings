import re
import collections
from collections import Counter
def vertical_histogram_of(s):
    s = re.sub('[a-z]*[0-9]*[\W_]*', '', s.replace(' ',''))
    counter = Counter(s)
    od = collections.OrderedDict(sorted(counter.items()))
    lst = [i for i in od]
    if len(s) == 0:
        return ''
    while True:
        step = ['*' if j > 0 else ' ' for i,j in od.items()] + ['\n']
        if '*' not in step:
            result = (' '.join(lst)).replace(' \n ','\n') 
            return re.sub('\* +\\n','*\n',result)
        lst = step + lst
        od = collections.OrderedDict([(i,j-1) for i,j in od.items()])
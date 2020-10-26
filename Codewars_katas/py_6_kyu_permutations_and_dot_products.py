import numpy
from itertools import permutations 
def min_dot(a, b):
    
    if len(b)!=0 and len(a)!=0 :
        return numpy.dot(sorted(a),sorted(b,reverse = True))
    else:
        return 0
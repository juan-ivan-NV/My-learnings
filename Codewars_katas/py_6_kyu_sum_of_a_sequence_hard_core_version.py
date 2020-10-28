import math
def sequence_sum(begin, end, step):
    
    change = math.floor((end-begin)/step)+1
    
    if change < 0:
        return 0
    
    else:
        c = begin+(change-1)*step
        result = (begin+c)*change//2
        return result 
import string
def high(x):
    
    y = x.split()
    scores = []
    
    for i in y:
        d = sum([(ord(j) - 97) for j in i])
        scores.append(d)
    
    maxindex = scores.index(max(scores))
    return y[maxindex]
def Xbonacci(signature,n):
    
    x = len(signature)
    result = signature
    
    for i in range(x,n):
        y = sum(result[-x:])
        result.append(y)
        
    return result[:n]
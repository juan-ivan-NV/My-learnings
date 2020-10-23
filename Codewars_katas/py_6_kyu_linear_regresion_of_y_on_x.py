def regressionLine(x, y):

    sx = 0
    sy = 0
    sxy = 0
    sx2 = 0
    a = 0
    
    for i in range(len(x)):
        
        sx += x[i]
        sx2 += x[i]**2
        sy += y[i]
        sxy += (x[i]*y[i])   
    
    a = ((sx2)*(sy) - (sx)*(sxy))/((len(x))*(sx2)-(sx)**2)
    b = ((len(x))*(sxy) - (sx)*(sy))/((len(x))*(sx2)-(sx)**2)
    
    return (round(a,4),round(b,4))
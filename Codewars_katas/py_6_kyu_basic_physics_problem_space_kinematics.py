def meeting_time(Ta, Tb, r):
    print(Ta, Tb)
    if Ta == 0 and Tb == 0:
        return '0.00'
    elif Ta == 0:
        return '%.2f'%abs(Tb)
    elif Tb == 0:
        return '%.2f'%abs(Ta)
    else:
        return '%.2f'%abs(2*3.1416/((2*3.1416)/Ta-(2*3.1416)/Tb))
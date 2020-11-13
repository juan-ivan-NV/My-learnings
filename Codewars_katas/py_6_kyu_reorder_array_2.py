import numpy as np

def reorder(n, m):
    arr1, arr2 = np.split(np.arange(n), 2)
    i = 1
    
    while i <= m:
        arr1 = np.roll(arr1.copy(),1)
        arr2 = np.roll(arr2.copy(),1)
        i += 1
        
    list_arr = [[x for x in arr1],[x for x in arr2]]
    return list_arr
def longest_consec(strarr, k):
    if k > len(strarr) or k == 0 or k <= 0:
        return ''
    concatenated = []
    for x in range(len(strarr)+1-k):
        concatenated.append(''.join([strarr[i] for i in range(x,x+k)]))
    return max(concatenated, key=len)
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1: primfac.append(n)
    return len(primfac)

def count_Kprimes(k, start, nd):
    return [i for i in range(start, nd+1) if primes(i)==k]

def puzzle(s):
    a, b, c = count_Kprimes(1, 2, s), count_Kprimes(3, 8, s), count_Kprimes(7, 128, s)
    return sum(i + j + k == s for i in a for j in b for k in c)
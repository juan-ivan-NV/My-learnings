def gen_primes(n):
    D = {}
    q = 2
    
    while q <= n:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def prime_string(m, k):
    if k < 1: return ''
    if k == 1: return '(%i)' % m
    return '(%i**%i)' % (m, k)

def primeFactors(n):
    if n < 3: return n
    s = ''
    for p in gen_primes(n/2):
        if n < 2: break
        if n%p != 0: continue
        ni = 0
        while n%p == 0:
            ni += 1
            n /= p
        s += prime_string(p, ni)
    if not s: return '(%i)' % n
    return s
import numpy as np
import math

def digits(N):
    i = 1
    while N // i:
        i *= 10
    return int(math.log10(i))

nthdigit = lambda n, N: (N // 10**n) % 10

digits2arr = lambda N: [nthdigit(n, N) for n in reversed(range(digits(N)))]

arr2digits = lambda a: sum([n * d for n, d in zip(a,[10**x for x in list(reversed(range(len(a))))])])

def nthdecimal(d, n):
    q = 1 // d
    r = 1 % d
    while n > 0:
        r *= 10
        q = r // d
        r = r % d
        n -= 1
    return q

fraction_decimals = lambda d, n: [nthdecimal(d, i) for i in range(1, n+1)]

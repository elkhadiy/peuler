import numpy as np
import importlib.resources

from numba import jit

from itertools import chain, combinations
from math import prod

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

MODULE_PATH = importlib.resources.files(__package__)

primes = np.load(MODULE_PATH / 'primes_1M.npz')['primes']

primeslesqrt = lambda N: primes[primes <= np.ceil(np.sqrt(N))]

def pwrfactor(N, f):
    n = 1
    while N % f**n == 0:
        n += 1
    return n-1

pwrfactors = lambda N, f: np.array([ np.vectorize(pwrfactor, excluded=['N'])(n, f) for n in np.ravel(N) ])

def factors(n):
    if n == 1:
        return np.array([[1, 1]])
    p = primes[primes <= n]
    f = np.column_stack((p, pwrfactors(n, p).flatten()))
    return f[f[:,1] > 0]


divisors = lambda n: np.unique([ np.prod(s) for s in powerset([ item for sublist in [ [e] * p for e, p in factors(n) ] for item in sublist ])]).astype('int')


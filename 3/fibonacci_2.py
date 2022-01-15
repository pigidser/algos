from functools import lru_cache

def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

fib1 = lru_cache(maxsize=None)(fib1)

print(fib1(80))
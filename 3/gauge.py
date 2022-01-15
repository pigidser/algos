import time

# Function fib1 with no decorator    
def fib1(n):
    assert n >= 0
    return n if n <=1 else fib1(n - 1) + fib1(n-2)

def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return 0 if n == 0 else f1

def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc

print(timed(fib3, 800))

import matplotlib.pyplot as plt

def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()

compare([fib3], list(range(500)))
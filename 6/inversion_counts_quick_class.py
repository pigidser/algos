"""Число инверсий
Первая строка содержит число 1 <= n <= 10^5, вторая — массив A[1..n], содержащий натуральные числа, не превосходящие 10^9.
Необходимо посчитать число пар индексов 1 <= i < j <= n, для которых A[i] > A[j].
(Такая пара элементов называется инверсией массива. Количество инверсий в массиве является в некотором смысле
его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)"""


import time
from random import randint

class InversionCounts:

    def __init__(self):
        self.acc = 0

    def __call__(self, A):
        self.acc = 0
        self._merge_sort(A)
        return self.acc


    def _merge(self, L, R):
        M = []
        l, r = 0, 0
        len_L, len_R = len(L), len(R)
        while l < len_L and r < len_R:
            if L[l] <= R[r]:
                M.append(L[l])
                l += 1
            else:
                self.acc += len_L - l
                M.append(R[r])
                r += 1
        return M + L[l:] + R[r:]


    def _merge_sort(self, A):
        l, r = 0, len(A) - 1
        if l < r:
            m = (l + r)//2
            return self._merge(self._merge_sort(A[:m+1]), self._merge_sort(A[m+1:]))
        else:
            return A


def main():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    ic = InversionCounts()
    print(ic(A))
    # A = [7,2,5,3,7,13,1,6]
    # # A = [2,3,9,2,9]
    # # A = [3,2,1]
    # # A = [1,2,3,5,4]
    # print(iter_merge_sort(A))
    # print(sum(acc))


def timed(f, *args, n_iter=10):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
        print(acc)
    return acc


def test():
    ic = InversionCounts()
    assert ic([3,2,1]) == 3
    assert ic([2,3,9,2,9]) == 2
    assert ic([4,3,2,1]) == 6
    assert ic([7,2,5,3,7,13,1,6]) == 13
    assert ic([7,6,5,4,3,2,1]) == 21
    assert ic([1,2,3,5,4]) == 1

    acc = float("inf")
    t0 = time.perf_counter()
    n = 10**5
    A = []
    for i in range(n):
        A.append(randint(0, 10**9))
    print(ic(A))
    t1 = time.perf_counter()
    print(min(acc, t1 - t0))
    

    for _ in range(10):
        n = randint(1, 10**5)
        A = []
        for i in range(n):
            A.append(randint(0, 10**9))
        t = timed(ic, A)
        print(t)
        assert t < 3

    print(f"All test passed!")

if __name__ == "__main__":
    test()
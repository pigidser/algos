"""Число инверсий
Первая строка содержит число 1 <= n <= 10^5, вторая — массив A[1..n], содержащий натуральные числа, не превосходящие 10^9.
Необходимо посчитать число пар индексов 1 <= i < j <= n, для которых A[i] > A[j].
(Такая пара элементов называется инверсией массива. Количество инверсий в массиве является в некотором смысле
его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)"""


import time
from random import randint

class InversionCouns:

    def __init__(self):
        self.acc = []

    def __call__(self, A):
        self.acc = []
        self._iter_merge_sort(A)
        return sum(self.acc)

    def _merge(self, L, R):
        M = []
        while L and R:
            if L[0] <= R[0]:
                el = L.pop(0)
            else:
                self.acc.append(len(L))
                el = R.pop(0)
            M.append(el)
        return M + L + R


    def _iter_merge_sort(self, A):
        Q = [[x] for x in A]
        while len(Q) > 1:
            if len(Q[0]) == 1 and len(Q[0]) < len(Q[1]):
                Q.append(Q.pop(0))
            else:
                Q.append(self._merge(Q.pop(0), Q.pop(0)))
        return Q[0]




def main():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    ic = InversionCouns()
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
    ic = InversionCouns()
    assert ic([7,2,5,3,7,13,1,6]) == 13
    assert ic([2,3,9,2,9]) == 2
    assert ic([3,2,1]) == 3
    assert ic([4,3,2,1]) == 6
    assert ic([7,6,5,4,3,2,1]) == 21
    assert ic([1,2,3,5,4]) == 1

    n = 10**5
    A = []
    for i in range(n):
        A.append(randint(0, 10**9))
    print(ic(A))

    # 
    # for _ in range(10):
    #     n = randint(1, 10**5)
    #     A = []
    #     for i in range(n):
    #         A.append(randint(0, 10**9))
    #     t = timed(ic, A)
    #     print(t)
    #     assert t < 3

    print(f"All test passed!")

if __name__ == "__main__":
    main()
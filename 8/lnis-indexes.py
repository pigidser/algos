"""
Задача на программирование повышенной сложности: наибольшая невозрастающая подпоследовательность
Дано целое число 1 <= n <= 10^5 и массив A[1...n], содержащий неотрицательные целые числа, не превосходящие 10^9.
Найдите наибольшую невозрастающую подпоследовательность в A. В первой строке выведите её длину k, во второй —
её индексы 1 <= i_1 < i_2 < ... < i_k < n (таким образом, A[i_1] >= A[i_2] >= ... >= A[i_n])


Sample Input:

5
5 3 4 4 2
Sample Output:

4
1 3 4 5

"""

import sys
import time
from random import randint


def lnis(A):
    # longest non-increasing subsequence
    D = [1] * len(A)
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] >= A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1  # количество элементов в наибольшей невозрастающей последовательности до i-го элемента
    return
    # # print(A)
    # # print(D)
    # max_s = D.index(max(D))
    # O = [max_s]
    # max_i = max_s
    # for i in range(max_s - 1, -1, -1):
    #     if D[i] + 1 == D[max_i] and A[i] >= A[max_i]:
    #         max_i = i
    #         O.append(max_i)
    # O = O[::-1]
    # # print(list(map(lambda x: x+1, O)))
    # return list(map(lambda x: x+1, O))

def main():
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    assert len(A) == n
    O = lnis(A)
    print(len(O))
    print(' '.join(map(str, O)))


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def test():
    
    # assert lnis([2]) == [1]
    # assert lnis([2, 3]) == [1]
    # assert lnis([2, 2]) == [1, 2]
    # assert lnis([3, 2]) == [1, 2]
    # assert lnis([5, 3, 4, 4, 2]) == [1, 3, 4, 5]
    # assert lnis([7, 6, 1, 6, 4, 1, 2, 4, 10, 1]) == [1, 2, 4, 5, 8, 10]

    n = 10**4
    A = []
    for i in range(n):
        A.append(randint(1, 10**9))

    print("GO!")
    t = timed(lnis, A)
    assert t < 5
    
    
    # for attempt in range(100):
    #     n = randint(1, 10**5)
    #     A = []
    #     for i in range(n):
    #         A.append(randint(1, 10**9))

    #     t = timed(lnis, A)
    #     assert t < 5

    print("All tests passed!")


if __name__ == "__main__":
    test()
"""
Задача на программирование: наибольшая последовательнократная подпоследовательность
Дано целое число 1 <= n <= 10^3 и массив A[1...n] натуральных чисел, не превосходящих 2 * 10^9.
Выведите максимальное 1 <= k <= n, для которого найдётся подпоследовательность 1 <= i1 < i2 < ... < ik <= n длины k,
в которой каждый элемент делится на предыдущий (формально: для  всех 1 <= j < k, A[ij] | A [ij+1]).

Sample Input:
4
3 6 7 12

Sample Output:
3

"""

import sys


def lcms(A):
    """
    Longest Consecutive Multiple Subsequence
    """
    D = [1] * len(A)
    for i in range(1, len(A)):
        for j in range(i):
            if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1  # количество элементов на которые i-й элемент делится без остатка
    return max(D)


def main():
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    assert len(A) == n
    print(lcms(A))


def test():
    
    assert lcms([2]) == 1
    assert lcms([2, 3]) == 1
    assert lcms([2, 2]) == 2
    assert lcms([3, 2]) == 1
    assert lcms([8,8,8,8,8]) == 5
    assert lcms([3,6,7,12]) == 3
    assert lcms([3,6,3,7,12]) == 3
    assert lcms([3,6,6,7,12]) == 4
    assert lcms([3, 4, 12, 8, 5, 4, 24, 1, 16, 24, 2, 6, 18, 4, 32, 12, 48, 13]) == 5
    assert lcms([2,6,7,7,12,21,36,42,84,168]) == 6
    assert lcms([3,6,12,7,9,24,18,3,9,24]) == 5
    assert lcms([2,6,3,7,4,1,9,2,12,3,8]) == 3
    assert lcms([2,4,8,16]) == 4
    assert lcms([1,2,2,4,6,12,36,8,7,9,16,48,48,3,9,48,96]) == 10
    assert lcms([2,2,3,6,12,8,16,32,64,768]) == 7
    assert lcms([1,2,2,]) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
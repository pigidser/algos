"""
В первой строке даны целое число 1 <= n <= 10^5 и массив A[1..n] из n различных натуральных чисел, не превышающих 10^9,
в порядке возрастания, во второй — целое число 1 <= k <= 10^5 и k натуральных чисел b_1,...b_k, не превышающих 10^9.
Для каждого i от 1 до k необходимо вывести индекс 1 <= j <= n, для которого A[j]=b_i, или -1, если такого j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
"""

import sys

def find(A, b):
    l, r = 0, len(A) - 1
    while l <= r:
        m = l + (r - l)//2
        if A[m] == b:
            return m + 1
        elif b < A[m]:
            r = m - 1
        else:
            l = m + 1
    else:
        return -1


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    line = next(reader)
    n, A = line[0], line[1:]
    assert len(A) == n
    line = next(reader)
    k, B = line[0], line[1:]
    assert len(B) == k
    print(" ".join(str(find(A, b)) for b in B))


def test_main():
    line1 = "5 1 5 8 12 1"
    line2 = "5 8 1 23 1 11"
    line3 = "3 1 -1 1 -1"
    line1 = list(map(int, line1.split()))
    line2 = list(map(int, line2.split()))
    n, A = line1[0], line1[1:]
    assert len(A) == n
    k, B = line2[0], line2[1:]
    assert len(B) == k
    assert " ".join(str(find(A, b)) for b in B) == line3

    line1 = "1 1"
    line2 = "2 0 1"
    line3 = "-1 1"
    line1 = list(map(int, line1.split()))
    line2 = list(map(int, line2.split()))
    n, A = line1[0], line1[1:]
    assert len(A) == n
    k, B = line2[0], line2[1:]
    assert len(B) == k
    assert " ".join(str(find(A, b)) for b in B) == line3

    print("All tests passed!")

    line1 = "1 1"
    line2 = "2 0 1"
    line3 = "-1 1"
    line1 = list(map(int, line1.split()))
    line2 = list(map(int, line2.split()))
    n, A = line1[0], line1[1:]
    assert len(A) == n
    k, B = line2[0], line2[1:]
    assert len(B) == k
    assert " ".join(str(find(A, b)) for b in B) == line3

    print("All tests passed!")


def test_find():
    A = list(map(int, "1 5 8 12 13".split()))
    assert find(A, 8) == 3
    assert find(A, 1) == 1
    assert find(A, 13) == 5
    assert find(A, 0) == -1
    A = list(map(int, "1".split()))
    assert find(A, 1) == 1
    assert find(A, 0) == -1

    print("All tests passed!")


if __name__ == "__main__":
    main()
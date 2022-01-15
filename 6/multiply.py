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

def multiply(x, y):
    print(x, y)
    return 2 * 3


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    x, y = next(reader)
    print(multiply(x, y))


if __name__ == "__main__":
    main()
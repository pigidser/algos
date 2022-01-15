"""
Наибольшая убывающая подпоследовательность

O(nlogn)

"""

# A = [2, 7, 1, 4, 3, 5, 4, 6, 2, 5, 8, 3]
A = [5, 3, 4, 4, 2, 5, 9]
n = len(A)

inf = max([abs(x) for x in A]) + 1
L = [inf] + [-inf] * (n + 1)

for i in range(n):
    left, right = 0, n + 1
    while left + 1 < right:
        middle = (left + right) // 2
        if L[middle] > A[i]:
            left = middle
        else:
            right = middle
    L[right] = A[i]


print(A)
print(L)

"""
Наибольшая возрастающая подпоследовательность

O(nlogn)

"""

A = [2, 7, 1, 4, 3, 5, 4, 6, 2, 5, 8, 3]
n = len(A)

# самое больше число по абсолютному значению
inf = max([abs(x) for x in A]) + 1

# Массив для хранения результатов функций L[i]
L = [-inf] + [inf] * (n + 1)

# Для всех элементов массива A выполнить двоичный поиск элемента A[i] в массиве результатов функций L[i]
for i in range(n):
    left, right = 0, n + 1
    while left + 1 < right:
        middle = (left + right) // 2
        if L[middle] < A[i]:
            left = middle
        else:
            right = middle
    # нашли позицию right в массиве L, которую нужно перезаписать значением A[i]
    L[right] = A[i]

print(A)
print(L)
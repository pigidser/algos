# Сортировка вставками

A = [5,2,3,1,2,8,3,4,5,6,7,1]

for i in range(1, len(A)):
    j = i
    while j > 0 and A[j] < A[j-1]:
        A[j], A[j-1] = A[j-1], A[j]
        j -= 1

print(A)
heap = list([0])


def sift_up(i):
    while i > 1 and heap[i//2] < heap[i]:
        heap[i//2], heap[i] = heap[i], heap[i//2]
        i = i//2


def sift_down(i):
    while 2*i <= len(heap) - 1:
        j = i
        if heap[2*i] > heap[j]:
            j = 2*i
        if (2*i + 1 <= len(heap) - 1) and (heap[2*i + 1] > heap[j]):
                j = 2*i + 1
        if j == i:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i = j

def insert(x):
    heap.append(x)
    i = len(heap) - 1
    sift_up(i)

def extract_max():
    print(heap[1])
    heap[1] = heap[len(heap) - 1]
    heap.pop(len(heap) - 1)
    sift_down(1)

def check_heap():
    for i in range(2, len(heap) - 1):
        assert heap[i] <= heap[i//2]
            

# n = int(input())
# for i in range(n):
#     operation = input()
#     if ' ' in operation:
#         insert(int(operation.split()[1]))
#     else:
#         extract_max()

# insert(200)
# insert(10)
# extract_max()
# insert(5)
# insert(500)
# extract_max()


elements = [9, 4, 1, 5, 10, 1, 3, 19, 4, 6, 2, 7, 1, 8, 3]
for item in elements:
    insert(item)

while len(heap) > 1:
    extract_max()
    print(heap)
    check_heap()


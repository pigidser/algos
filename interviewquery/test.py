ints = [1, 5, 6, 9, 11, 14, 22, 91, 100]
print(ints.index(9))


# import heapq

# # ints = [1,2,3,4,5,6,7,8,9]
# # N = 4
# # k = 2
# # ints = [1,3,4,6,8]
# # N = 5
# # k = 1

# ints = [1, 5, 6, 9, 11, 14, 22, 91, 100]
# print(ints.index(9))
# N = 4
# k = 2

# dist = [(abs(N - elem), - (N - elem), elem) for elem in ints]

# heapq.heapify(dist)

# neg = k + 1
# pos = k
# k_nearest = list()
# while neg or pos:
#     elem = heapq.heappop(dist)
#     if elem[1] <= 0 and neg > 0:
#         neg -= 1
#         k_nearest.append(elem)
#     elif elem[1] > 0 and pos > 0:
#         pos -= 1
#         k_nearest.append(elem)

# print(sorted(k_nearest))
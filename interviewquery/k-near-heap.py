import heapq
import random
def nearest_entries(ints, N, k):
    dist = [(abs(N - elem), - (N - elem), elem) for elem in ints]
    heapq.heapify(dist)
    ind = ints.index(heapq.heappop(dist)[2])
    return ints[max(ind - k, 0): min(ind + k + 1, len(ints))]

def main():
    # ints = list(map(int, input().split()))
    # N, k = list(map(int, input().split()))
    ints = [i for i in range(10**8)]
    print("checkpoint 1")
    N = 9999
    k = 30
    # ints = [1,2,3,4,5,6,7,8,9]
    # N = 5
    # k = 2
    k_nearest = nearest_entries(ints, N, k)
    print(k_nearest)

if __name__ == "__main__":
    main()
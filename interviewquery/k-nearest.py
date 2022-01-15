def nearest_entries(ints, N, k):
    l, m, r = 0, 0, len(ints) - 1
    while l < r:
        m = l + (r - l) // 2 + (r - l) % 2
        if ints[m] == N:
            break
        elif N < ints[m]:
            m -= 1
            r = m
        else:
            l = m
    # Now m is index of required element 
    # Get k-nearest
    print(m, ints[m])
    return ints[max(m - k, 0): min(m + k + 1, len(ints))]


def main():
    # ints = list(map(int, input().split()))
    # N, k = list(map(int, input().split()))
    # ints = [1, 5, 6, 9, 11, 14, 22, 91, 100]
    # N = 12
    # k = 2
    ints = [1, 5, 6, 9, 11, 14, 22, 91, 100]
    N = 4
    k = 2
    k_nearest = nearest_entries(ints, N, k)
    print(k_nearest)

if __name__ == "__main__":
    main()
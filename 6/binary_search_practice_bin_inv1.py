import sys

def find_pos(xs, query):
    # Invariant: lo <= pos < hi
    lo, hi = 0, len(xs)
    while lo < hi:
        mid = (lo + hi) // 2
        if query < xs[mid]:         # [lo, mid)
            hi = mid
        elif query > xs[mid]:       # [mid + 1, hi)
            lo = mid + 1
        else:
            return mid + 1
    
    return - 1

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")

if __name__ == '__main__':
    main()
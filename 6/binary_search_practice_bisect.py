import sys
from bisect import bisect_left

def find_pos(xs, query):
    lo = bisect_left(xs, query)
    # i < lo : xs[i] < query
    # i > lo : xs[i] >= query
    if lo < len(xs) and xs[lo] == query:
        return lo + 1       # 1-based
    else:
        return - 1

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")

if __name__ == '__main__':
    main()
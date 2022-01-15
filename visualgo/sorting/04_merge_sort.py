import sys


def merge(L, R):
    M = []
    l, r = 0, 0
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            el = L[l]
            l += 1
        else:
            el = R[r]
            r += 1
        M.append(el)
    if l < len(L):
        M = M + L[l:]
    if r < len(R):
        M = M + R[r:]
    return M


def merge_sort_recurr(arr):
    l, r = 0, len(arr) - 1
    if l < r:
        m = (l + r)//2
        return merge(merge_sort_recurr(arr[ : m+1]), merge_sort_recurr(arr[m+1 : ]))
    else:
        return arr


def merge_sort_queue(arr):
    if not len(arr): return arr
    Q = [[x] for x in arr]
    while len(Q) > 1:
        Q.append(merge(Q.pop(0), Q.pop(0)))
    return Q[0]


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    input_array = next(reader)
    print(' '.join(map(str, merge_sort_queue(input_array))))


def test():
    import test_sort
    # test_sort.test(merge_sort_recurr)
    test_sort.test(merge_sort_queue)


if __name__ == "__main__":
    test()


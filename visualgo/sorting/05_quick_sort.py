import sys
import random

def partition(a, i, j):
    p = a[i]                            # p is the pivot
    m = i                               # S1 and S2 are initially empty
    for k in range(i + 1, j + 1):       # explore the unknown region
        if a[k] < p:                    # case 2
            m += 1
            a[k], a[m] = a[m], a[k]
        # notice that we do nothing in case 1: a[k] >= p
    a[i], a[m] = a[m], a[i]             # final step, swap pivot with a[m]
    return m                            # return the index of pivot


def quick_sort(a, low, high):
    if low < high:
        m = partition(a, low, high)
        # a[low..high] ~> a[low..m–1], pivot, a[m+1..high]
        quick_sort(a, low, m)       # recursively sort left subarray
        # a[m] = pivot is already sorted after partition
        quick_sort(a, m + 1, high)  # then sort right subarray
    return a


def do_sort(input_array):
    return quick_sort(input_array, 0, len(input_array) - 1)


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    input_array = next(reader)
    print(' '.join(map(str, do_sort(input_array))))


def test():
    import test_sort
    # test_sort.test(merge_sort_recurr)
    test_sort.test(do_sort)


if __name__ == "__main__":
    test()


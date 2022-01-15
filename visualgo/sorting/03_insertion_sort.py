import sys

def insertion_sort(arr):

    len_arr = len(arr)

    for i in range(1, len_arr):
        X = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > X:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = X
    print(arr)
    return arr


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    input_array = next(reader)
    print(' '.join(map(str, insertion_sort(input_array))))


def test():
    import test_sort
    test_sort.test(insertion_sort)


if __name__ == "__main__":
    test()


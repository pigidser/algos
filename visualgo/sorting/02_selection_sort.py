import sys

def selection_sort(arr):

    len_arr = len(arr)
    firstUnsorted = 0

    while firstUnsorted < len_arr - 1:
        currentMinimum = firstUnsorted
        for i in range(firstUnsorted + 1, len_arr):
            if arr[i] < arr[currentMinimum]:
                currentMinimum = i
        arr[firstUnsorted], arr[currentMinimum] = arr[currentMinimum], arr[firstUnsorted]
        firstUnsorted += 1
    return arr


def selection_sort_reversed(arr):

    lastUnsorted = len(arr) - 1

    while lastUnsorted >= 0:
        currentMinimum = lastUnsorted
        for i in range(lastUnsorted - 1, -1, -1):
            if arr[i] > arr[currentMinimum]:
                currentMinimum = i
        arr[lastUnsorted], arr[currentMinimum] = arr[currentMinimum], arr[lastUnsorted]
        lastUnsorted -= 1
    return arr


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    input_array = next(reader)
    print(' '.join(map(str, selection_sort(input_array))))


def test():
    import test_sort
    test_sort.test(selection_sort)


if __name__ == "__main__":
    main()


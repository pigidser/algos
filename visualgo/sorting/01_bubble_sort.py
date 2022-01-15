import sys

def bubble_sort(arr):
    indexOfLastUnsortedElement = max(0, len(arr) - 1)

    while indexOfLastUnsortedElement:
        for i in range(indexOfLastUnsortedElement):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        indexOfLastUnsortedElement -= 1
    return arr


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    input_array = next(reader)
    print(' '.join(map(str, bubble_sort(input_array))))


def test():
    import test_sort
    test_sort.test(bubble_sort)

if __name__ == "__main__":
    main()
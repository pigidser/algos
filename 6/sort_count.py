def sort_count(A):

    cnt = dict()
    for i in range(len(A)):
        if A[i] in cnt:
            cnt[A[i]] += 1
        else:
            cnt[A[i]] = 1

    A1 = list()
    for i in range(max(A) + 1):
        if i in cnt:
            A1 += [i] * cnt[i]

    return A1


def main():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    print(sort_count(A))


def test():

    A = [2,4,5,2,1]
    A1 = sort_count(A)
    print(A1)
    assert A1 == [1,2,2,4,5]

    A = [2,1]
    A1 = sort_count(A)
    print(A1)
    assert A1 == [1,2]

    A = [1]
    A1 = sort_count(A)
    print(A1)
    assert A1 == [1]

    print("All tests passed") 


if __name__ == "__main__":
    main()
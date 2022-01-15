

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


def merge_sort(A):
    l, r = 0, len(A) - 1
    if l < r:
        m = (l + r)//2
        return merge(merge_sort(A[:m+1]), merge_sort(A[m+1:]))
    else:
        return A


def main():
    A = [7,2,5,3,7,13,1,6]
    print(f"initial: {A}")
    M = merge_sort(A)
    print(f"sorted : {M}")


def test_merge():
    L = [1,3,4,6,9]
    R = [1,2,5,7,8]
    M = merge(L, R)
    print(M)
    assert len(M) == len(L) + len(R)
    assert M == [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    L = [1]
    R = [1,2]
    M = merge(L, R)
    print(M)
    assert len(M) == len(L) + len(R)
    assert M == [1, 1, 2]

    L = []
    R = [1,2]
    M = merge(L, R)
    print(M)
    assert len(M) == len(L) + len(R)
    assert M == [1, 2]

    L = []
    R = []
    M = merge(L, R)
    print(M)
    assert len(M) == len(L) + len(R)
    assert M == []


def test_merge_sort():
    A = [7,2,5,3,7,13,1]
    print(merge_sort(A))

if __name__ == "__main__":
    main()
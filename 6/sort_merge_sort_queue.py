

def merge(L, R):
    M = []
    l, r = 0, 0
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            el = L[l]
            l += 1
        else:
            print(1)
            el = R[r]
            r += 1
        M.append(el)
    if l < len(L):
        M = M + L[l:]
    if r < len(R):
        M = M + R[r:]
    return M


def iter_merge_sort(A):
    Q = [[x] for x in A]
    while len(Q) > 1:
        Q.append(merge(Q.pop(0), Q.pop(0)))
    return Q[0]


def main():
    A = [7,2,5,3,7,13,1,6]
    print(f"initial: {A}")
    M = iter_merge_sort(A)
    print(f"sorted : {M}")



if __name__ == "__main__":
    main()
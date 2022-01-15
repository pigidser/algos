def fib_mod(n, m):

    p = [0, 1]
    left = 0

    for i in range(2, n + 1):
        # Add (mod m) values in the row
        p.append( (p[i-2] + p[i-1]) % m )
        # From the third element, we start to monitor similarity the current values with the first ones.
        if (i >= 3):
            if p[i] == p[left]:
                if left == 0:
                    # Set the right border index that probably is the period
                    right = i
                elif left == right:
                    # We checked that elements in the first and second periods are the same.
                    # In the case n is large than period, add from mod division.
                    return p[right + (n % right)]
                # In the next cicle we will check the second element
                left += 1
            else:
                left = 0

    else:
        return p[-1]


def main():

    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
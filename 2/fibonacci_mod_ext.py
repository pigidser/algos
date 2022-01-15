"""
Даны целые числа 1 <= n <= 10^18 и 2 <= m <= 10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.

"""
def fib(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-2] + f[i-1])
    return f[n]


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

def fib_mod_2(n, m):
    o,i=[0,1],2
    while not (o[i-2]==0 and o[i-1]==1) or i<=2:
        o.append((o[i-2]+o[i-1])%m)
        i+=1

    return o[n%(i-2)]

def fib_mod_3(n, m):
    p = [0, 1]
    x, y = 0, 1
    for i in range(6*m):
        x, y = y, (x+y)%m
        p.append(y % m)
        if p[-1] == 1 and p[-2] == 0:
            break
        
    return p[n%(len(p)-2)]

def main():

    # n, m = map(int, input().split())

    N = 10**3
    m = 30

    # print(fib_mod(n, m))

    for n in range (1, N):
        assert( fib_mod(n, m) == (fib(n) % m) )
    print("Passed fib_mod")

    for n in range (1, N):
        assert( fib_mod_2(n, m) == (fib(n) % m) )
    print("Passed fib_mod_2")

    for n in range (1, N):
        assert( fib_mod_3(n, m) == (fib(n) % m) )
    print("Passed fib_mod_3")

if __name__ == "__main__":
    main()
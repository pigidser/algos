"""
Дано целое число 1 <=n <= 40, необходимо вычислить n-е число Фибоначчи.
Sample Input:
3
Sample Output:
2

"""
def fib(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-2] + f[i-1])
    return f[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
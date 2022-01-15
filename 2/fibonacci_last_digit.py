"""
Дано число 1 <= n <= 10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.
Известно, что если a и b - последние цифры чисел Fi и F(i+1) соответственно, то последняя цифра числа F(i+2)
будет равна (a + b) mod 10.

"""
def fib_digit(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append((f[i-2] + f[i-1]) % 10)
    return f[n]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
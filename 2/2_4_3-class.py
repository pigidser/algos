from sympy import Symbol, limit, log, factorial, oo

'''
класс - обертка для выражения sympy
для работы достаточно реализовать перегрузку оператора __lt__ (хотя надо бы и __le__ и остальные тоже перегружать)
'''
class ExpessionWrapper:
    def __init__(self, expr):
        self.expression = expr
    def __lt__(self, other):
        return limit(self.expression / other.expression, n, oo) == 0

if __name__ == "__main__":
    n = Symbol('n')

    funcs = [7**log(n, 2), 2**(3*n), n**0.5, n / log(n, 5), factorial(n), n**(n**0.5), log(n, 2)**2,
        4**n, 3**log(n, 2), n**2, 2**n, log(n, 4)**0.5, 2**(2**n), n**log(n, 2), log(n, 2)**log(n, 2),
        log(factorial(n), 2), log(n, 3), log(log(n, 2), 2)]

    for func in sorted(list(map(lambda x: ExpessionWrapper(x), funcs))):
        print(func.expression)
from sympy import limit, Symbol, oo, log, sqrt, factorial
from sympy.core.numbers import Infinity

n = Symbol('n')

y1 = (1, 7**log(n, 2))
y2 = (2, 2**(3*n))
y3 = (3, n**0.5)
y4 = (4, n / log(n, 5))
y5 = (5, factorial(n))
y6 = (6, n**(n**0.5))
y7 = (7, log(n, 2)**2)
y8 = (8, 4**n)
y9 = (9, 3**log(n, 2))
y10 = (10, n**2)
y11 = (11, 2**n)
y12 = (12, log(n, 4)**0.5)
y13 = (13, 2**(2**n))
y14 = (14, n**log(n, 2))
y15 = (15, log(n, 2)**log(n, 2))
y16 = (16, log(factorial(n), 2))
y17 = (17, log(n, 3))
y18 = (18, log(log(n, 2), 2))

expr = list([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18])


# Bubble sort

indexOfLastUnsortedElement = len(expr)

while True:
    
    print(indexOfLastUnsortedElement)
    swapped = False
    for i in range (1, indexOfLastUnsortedElement):
        limit_expr = limit(expr[i-1][1]/expr[i][1], n, oo)
        if isinstance(limit_expr, Infinity):
            expr[i], expr[i-1] = expr[i-1], expr[i]
            swapped = True

    indexOfLastUnsortedElement -= 1
            
    if not swapped:
        break
        
print(expr)
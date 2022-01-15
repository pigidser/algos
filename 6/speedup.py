from math import log

soot = [[1, 2, 0], 
        [5, 2, 1], 
        [9, 3, 2], 
        [6, 4, 3], 
        [3, 2, 1], 
        [5, 4, 1], 
        [5, 4, 2], 
        [2, 2, 1], 
        [2, 3, 0]]


def comp(x):
    n = int(10e100)
    ab = log(x[0], x[1])
    d = x[2]
    
    if d > ab:
        return n ** x[2]
    elif d == ab:
        return n ** x[2] * log(n)
    else:
        return n ** ab
        
          
print(soot)
print(sorted(soot, key=comp))
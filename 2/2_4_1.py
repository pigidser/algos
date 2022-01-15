import math

r1_prev, r2_prev = 0, 0
for n in range (10, 1000, 50):

    # # 1 - True, 2 - False - растет одинаково 
    # r1 = 2**n
    # r2 = 2**(n+1)

    # # 3 - True - растет не быстрее
    # r1 = n * 2**n
    # r2 = 3**n

    # # 4 - True - растет одинаково
    # r1 = math.log(2*n, 3)
    # r2 = math.log(3*n, 2)

    # # 5 - True - растет не медленнее
    # r1 = n**2 / math.log(n, 3)
    # r2 = n * math.log(n, 2)**2

    # # 6 - False - растет не быстрее
    # r1 = 10 * math.log(n, 2)
    # r2 = math.log(n, 2)**2

    # 7 - True - растет не медленнее
    r1 = 3*n + 5
    r2 = n

    if r1_prev != 0 and r2_prev != 0:
        print(f"{r1:35}, {r2:50}, {'less' if r1 < r2 else 'greater'}, {r1/r1_prev:e}, {r2/r2_prev:e}")

    r1_prev, r2_prev = r1, r2

    if n >= 30:
        r1_30, r2_30 = r1, r2


print(f"{r1/r1_30:e}, {r2/r2_30:e}")

""" Непрерывный рюкзак.
Вариант с вводом sys.stdin. Для запуска из консоли:
python cont_backpack_stdin.py < values_and_weights.txt

Первая строка содержит количество предметов 1 <= n <= 10^3 и вместимость рюкзака 0 <= W <= 2*10^6.
Каждая из следующих nn строк задаёт стоимость 0 <= Ci <= 2*10^6 и объём 0 <= Wi <= 2*10^6 предмета. Все числа целые.
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30

Sample Output:
180.000

"""

import sys

reader = (tuple(map(int, line.split())) for line in sys.stdin)
n, W = next(reader)
S = list(reader)
S = sorted(S, key=lambda x: x[0]/x[1], reverse=True)

total, W_r = 0, W
for c, w in S:
    if W_r <= 0:
        break
    total += c if W_r >= w else W_r*c/w
    W_r -= w

print(f"{total :.3f}")
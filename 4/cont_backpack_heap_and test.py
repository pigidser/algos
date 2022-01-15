""" Непрерывный рюкзак.
Вариант с вводом sys.stdin и min-кучей. Для запуска из консоли:
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

import heapq
import sys
import time

def build_backpack(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)

    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        acc -= v_per_w * can_take
        capacity -= can_take

    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = list(reader)
    assert n == len(values_and_weights)
    value = build_backpack(capacity, values_and_weights)
    print(f"{value :.3f}")

def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc

def test():
    assert build_backpack(0, [(60, 20)]) == 0.0
    assert build_backpack(25, [(60, 20)]) == 60.0
    assert build_backpack(25, [(60, 20), (0, 100)]) == 60.0
    assert build_backpack(25, [(60, 20), (50, 50)]) == 60.0 + 5.0

    assert build_backpack(50, [(60, 20), (100, 50), (120, 30)]) == 180.0

    from random import randint
    for attempt in range(100):
        n = randint(1, 1000)
        capacity = randint(0, 2 * 10**6)
        values_and_weights = []
        for i in range(n):
            values_and_weights.append(
                (randint(0, 2 * 10**6), randint(1, 2 * 10**6)))
        t = timed(build_backpack, capacity, values_and_weights)
        assert t < 5

if __name__ == '__main__':
    test()
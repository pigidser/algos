# Это неоптимальное решение использует много памяти

"""
Точки и отрезки
В первой строке задано два целых числа 1 <= n <= 50000 и 1 <= m <= 50000 —
количество отрезков и точек на прямой, соответственно.
Следующие n строк содержат по два целых числа a_i и b_i (a_i <= b_i) —
координаты концов отрезков. Последняя строка содержит m целых чисел —
координаты точек. Все координаты не превышают 10^8 по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

"""

import numpy as np
# n, m = list(map(int, input().split()))
# lines = [tuple(map(int, input().split())) for _ in range(n+1)]
# points = list(map(int, input().split()))

# n, m = 10, 3
# lines = [(1, 4),(1, 3),(0, 1),(3, 6),(7, 10),(6, 7),(5, 6),(5, 7),(3, 6),(0, 2),]
# points = [1, 6, 11]


class Belonging():

    def __init__(self, lines):
        self.lines = lines
        self.min = min(lines, key=lambda x: x[0])[0]
        self.max = max(lines, key=lambda x: x[1])[1]
        self.calc_dist()

    def calc_dist(self):
        if self.min < 0:
            self.dist_neg = np.zeros(abs(self.min) + 1, dtype=int)
        if self.max >= 0:
            self.dist_pos = np.zeros(self.max + 1, dtype=int)
        for line in self.lines:
            if line[0] < 0:
                # The start of the segment lies to the left of zero
                # and the end can lie anywhere.
                self.dist_neg[abs(min(line[1], 0)):abs(line[0]) + 1] += 1
                # Check the end and update positive if neccessary
                if line[1] >= 0:
                    self.dist_pos[0:line[1] + 1] += 1
            else:
                self.dist_pos[line[0]:line[1] + 1] += 1

    def __call__(self, points):
        result = []
        for point in points:
            if point < self.min or self.max < point:
                result.append(0)
            else:
                if point < 0:
                    result.append(self.dist_neg[abs(point)])
                else:
                    result.append(self.dist_pos[point])
        return result


def main():
    pass

def test():
    # n, m = 10, 3
    # lines = [(1, 4),(1, 3),(0, 1),(3, 6),(7, 10),(6, 7),(5, 6),(5, 7),(3, 6),(0, 2),]
    # points = [1, 6, 11]
    # assert len(lines) == n and len(points) == m
    # bel = Belonging(lines)
    # res = bel(points)
    # print(res)
    # assert res == [4, 5, 0]

    # n, m = 2, 3
    # lines = [(0, 5),(7, 10)]
    # points = [1, 6, 11]
    # assert len(lines) == n and len(points) == m
    # bel = Belonging(lines)
    # res = bel(points)
    # print(res)
    # assert res == [1, 0, 0]

    # n, m = 1, 1
    # lines = [(0, 5)]
    # points = [1]
    # assert len(lines) == n and len(points) == m
    # bel = Belonging(lines)
    # res = bel(points)
    # print(res)
    # assert res == [1]

    # n, m = 1, 1
    # lines = [(0, 5)]
    # points = [6]
    # assert len(lines) == n and len(points) == m
    # bel = Belonging(lines)
    # res = bel(points)
    # print(res)
    # assert res == [0]

    # n, m = 2, 6
    # lines = [(-5, 5),(-1, 12)]
    # points = [-9, -4, 0, 2, 11, 17]
    # assert len(lines) == n and len(points) == m
    # bel = Belonging(lines)
    # res = bel(points)
    # print(res)
    # assert res == [0, 1, 2, 2, 1, 0]

    # n, m = 2, 6
    # lines = [(-5, 0),(-1, 12)]
    # points = [-9, -4, 0, 2, 11, 17]
    # assert len(lines) == n and len(points) == m
    # bel = Belonging(lines)
    # res = bel(points)
    # print(res)
    # assert res == [0, 1, 2, 1, 1, 0]

    import random
    from pympler import asizeof

    n, m = 1000, 1000
    lines = []
    for i in range(n):
        l = random.randint(0, 10**8)
        r = random.randint(l, 10**8)
        lines.append((l, r))
    points = [random.randint(0, 10**8) for _ in range(m)]

    assert len(lines) == n
    assert len(points) == m
    # print(lines)
    # print(points)

    bel = Belonging(lines)
    print(asizeof.asized(bel, detail=1).format())
    # print(bel(points))

    print(bel.min, bel.max)

    print("All tests passed!")


if __name__ == '__main__':
    test()






# assert len(lines) == n
# assert len(points) == m

# def belonging(lines, points):
# lines = sorted(lines, key=lambda x: x[0] + x[1])
# l, r = lines[0][0], lines[n-1][1]

# dist = np.zeros(lines[n-1][1], dtype=int)
# for line in lines:
#     dist[line[0]:line[1]+1] += 1

# output = []
# for point in points:
#     if l <= point and point <= r: 
#         output.append(dist[point])
#     else:
#         output.append(0)
# # lut = {}
# # for i in range(lines[0][0], lines[n-1][1]):

# # print(lines, points, dist)

# print(' '.join(map(str, output)))
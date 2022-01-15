# Success
"""
https://stepik.org/lesson/13249/step/6?unit=3434
Точки и отрезки
В первой строке задано два целых числа 1 <= n <= 50000 и 1 <= m <= 50000 —
количество отрезков и точек на прямой, соответственно.
Следующие n строк содержат по два целых числа a_i и b_i (a_i <= b_i) —
координаты концов отрезков. Последняя строка содержит m целых чисел —
координаты точек. Все координаты не превышают 10^8 по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

"""

import sys

class Belonging():

    def __init__(self, lines):
        self.lines_left = sorted(lines, key=lambda x: x[0])
        self.lines_right = sorted(lines, key=lambda x: x[1])
        self.len = len(lines)

    def _bin_search_right(self, b):
        l, r = 0, self.len - 1
        while l <= r:
            m = l + (r - l)//2
            if self.lines_right[m][1] == b:
                if m == l:
                    return m
                elif m == r and self.lines_right[m - 1][1] < b:
                    return m
                else:
                    r -= 1
            elif b < self.lines_right[m][1]:
                r = m - 1
            else:
                m += 1
                l = m
        return -1 if m > self.len - 1 else m

    def _bin_search_left(self, b):
        l, r = 0, self.len - 1
        while l <= r:
            m = l + (r - l)//2
            if self.lines_left[m][0] == b:
                if m == r:
                    return m
                elif m == l and b < self.lines_left[m + 1][0]:
                    return m
                else:
                    l += 1
            elif b < self.lines_left[m][0]:
                m -= 1
                r = m
            else:
                l = m + 1
        return m
            
    def bel_number(self, point):
        # Find the index of the most right segment with the start less or equal to our point
        right = self._bin_search_left(point)
        if right == -1:
            return 0
        # Among the segments with the start less or equal to our point find the index
        # of the most left segment with the end great or equal to our point
        left = self._bin_search_right(point)
        if left == -1:
            return 0
        return right - left + 1

    def __call__(self, points):
        result = []
        solved = {}
        for point in points:
            if point not in solved:
                solved[point] = self.bel_number(point)
            result.append(solved[point])

        return result


def main():
    
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, m = next(reader)
    lines = list(reader)
    points = lines.pop(-1)

    bel = Belonging(lines)
    print(' '.join(map(str, bel(points))))



def test_bin_search_right():

    lines = [(-100, 1)]
    bel = Belonging(lines)
    assert bel._bin_search_right(0) == 0
    assert bel._bin_search_right(1) == 0
    assert bel._bin_search_right(2) == -1

    lines = [(-100, 1), (-100, 1)]
    bel = Belonging(lines)
    assert bel._bin_search_right(0) == 0
    assert bel._bin_search_right(1) == 0
    assert bel._bin_search_right(2) == -1

    lines = [(-100, 1), (-100, 1), (-100, 1)]
    bel = Belonging(lines)
    assert bel._bin_search_right(0) == 0
    assert bel._bin_search_right(1) == 0
    assert bel._bin_search_right(2) == -1

    lines = [(-100, 1), (-100, 1), (-100, 2)]
    bel = Belonging(lines)
    assert bel._bin_search_right(0) == 0
    assert bel._bin_search_right(1) == 0
    assert bel._bin_search_right(2) == 2
    assert bel._bin_search_right(3) == -1

    print("All tests passed!")

def test_bin_search_left():

    lines = [(1, 10)]
    bel = Belonging(lines)
    assert bel._bin_search_left(0) == -1
    assert bel._bin_search_left(1) == 0
    assert bel._bin_search_left(2) == 0

    lines = [(1, 10),(2,10)]
    bel = Belonging(lines)
    assert bel._bin_search_left(0) == -1
    assert bel._bin_search_left(1) == 0
    assert bel._bin_search_left(2) == 1
    assert bel._bin_search_left(5) == 1

    lines = [(1, 10),(1,10)]
    bel = Belonging(lines)
    assert bel._bin_search_left(0) == -1
    assert bel._bin_search_left(1) == 1
    assert bel._bin_search_left(2) == 1
    assert bel._bin_search_left(5) == 1

    lines = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 6), (3, 6), (5, 6), (5, 7), (6, 7), (7, 10)]
    bel = Belonging(lines)
    assert bel._bin_search_left(-10) == -1
    assert bel._bin_search_left(0) == 1
    assert bel._bin_search_left(1) == 3
    assert bel._bin_search_left(2) == 3
    assert bel._bin_search_left(7) == 9
    assert bel._bin_search_left(15) == 9

    print("All tests passed!")


def test():


    n, m = 10, 5
    lines = [(-2, -1), (-2, 3), (-1, 0), (-1, 3), (0, 1), (0, 3), (1, 2), (1, 3), (2, 3), (2, 3)]
    points = [-3, -1, 0, 2, 3]
    assert len(lines) == n and len(points) == m
    bel = Belonging(lines)
    res = bel(points)
    print(res)
    assert res == [0, 4, 5, 7, 6]

    n, m = 10, 3
    lines = [(1, 4),(1, 3),(0, 1),(3, 6),(7, 10),(6, 7),(5, 6),(5, 7),(3, 6),(0, 2),]
    points = [1, 6, 11]
    assert len(lines) == n and len(points) == m
    bel = Belonging(lines)
    res = bel(points)
    print(res)
    assert res == [4, 5, 0]

    n, m = 2, 3
    lines = [(0, 5),(7, 10)]
    points = [1, 6, 11]
    assert len(lines) == n and len(points) == m
    bel = Belonging(lines)
    res = bel(points)
    print(res)
    assert res == [1, 0, 0]

    n, m = 1, 1
    lines = [(0, 5)]
    points = [1]
    assert len(lines) == n and len(points) == m
    bel = Belonging(lines)
    res = bel(points)
    print(res)
    assert res == [1]

    n, m = 1, 1
    lines = [(0, 5)]
    points = [6]
    assert len(lines) == n and len(points) == m
    bel = Belonging(lines)
    res = bel(points)
    print(res)
    assert res == [0]

    n, m = 2, 6
    lines = [(-5, 5),(-1, 12)]
    points = [-9, -4, 0, 2, 11, 17]
    assert len(lines) == n and len(points) == m
    bel = Belonging(lines)
    res = bel(points)
    print(res)
    assert res == [0, 1, 2, 2, 1, 0]

    n, m = 2, 6
    lines = [(-5, 0),(-1, 12)]
    points = [-9, -4, 0, 2, 11, 17]
    assert len(lines) == n and len(points) == m
    bel = Belonging(lines)
    res = bel(points)
    print(res)
    assert res == [0, 1, 2, 1, 1, 0]


    import random

    n, m = 50000, 50000
    lines = []
    for i in range(n):
        l = -10**7
        r = 10**7
        lines.append((l, r))
    points = [random.randint(0, 10**8) for _ in range(m)]

    assert len(lines) == n
    assert len(points) == m
    # print(lines)
    # print(points)

    bel = Belonging(lines)
    res = bel(points)

    # import random
    # from pympler import asizeof

    # n, m = 50000, 50000
    # lines = []
    # for i in range(n):
    #     l = random.randint(0, 10**8)
    #     r = random.randint(l, 10**8)
    #     lines.append((l, r))
    # points = [random.randint(0, 10**8) for _ in range(m)]

    # assert len(lines) == n
    # assert len(points) == m
    # # print(lines)
    # # print(points)

    # bel = Belonging(lines)
    # res = bel(points)
    # print(asizeof.asized(bel, detail=1).format())
    
    # print(bel.min, bel.max)

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
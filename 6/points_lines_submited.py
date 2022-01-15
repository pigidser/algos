"""
Usage: python points_lines_submited.py < points_lines.txt

"""

import numpy as np
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
    
    
if __name__ == '__main__':
    main()
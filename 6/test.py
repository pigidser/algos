import bisect

lines = [(1, 4),(1, 3),(0, 1),(3, 6),(7, 10),(6, 7),(5, 6),(5, 7),(3, 6),(0, 2),]
a, b = map(sorted, zip(*lines))

# a = sorted(a)
# b = sorted(b)
print(a, b)
right = bisect.bisect_right(a, 3)
left = bisect.bisect_left(b, 3)
print(right, left, right - left)
# lines = sorted(lines, key=lambda x: x[0] + x[1])
# lines = sorted(lines)
# print(lines)
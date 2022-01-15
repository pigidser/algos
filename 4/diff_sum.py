n = int(input())

s, i = 0, 1
while i < n - (s + i):
    s += i
    i += 1

out = list(range(1, i))
if n - s > 0:
    out.append(n-s)

print(str(len(out)) + "\n" + ' '.join(map(str, out)))

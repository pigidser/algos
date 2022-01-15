n = int(input())
nominals = [25, 10, 5, 1]
nominals.sort(reverse=True)
ex_set = list()
rem = n
for nominal in nominals:
    if rem >= nominal:
        cnt = rem // nominal
        rem %= nominal
        ex_set.append((nominal, cnt))

print(ex_set)
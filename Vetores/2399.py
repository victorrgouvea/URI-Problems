n = int(input())
v = []
p = []

for _ in range(0, n):
    b = int(input())
    v.append(b)

for _ in range(0, n):
    p.append(0)

for i in range(0, n):
    if v[i] == 1 and i == 0:
        p[i] += 1
        p[i+1] += 1
    elif v[i] == 1 and i == (n-1):
        p[i-1] += 1
        p[i] += 1
    elif v[i] == 1:
        p[i-1] += 1
        p[i] += 1
        p[i+1] += 1

for i in range(0, n):
    print(p[i])
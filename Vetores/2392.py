n, m = input().split()
n = int(n)
m = int(m)

v = [0] * (n)

for i in range(0, m):
    p, d = input().split()
    p = int(p)
    d = int(d)
    p -= 1
    v[p] = 1
    e = p - d
    f = p + d

    while e >= 0:
        v[e] = 1
        e -= d

    while f < n:
        v[f] = 1
        f += d

for i in v:
    print(i)
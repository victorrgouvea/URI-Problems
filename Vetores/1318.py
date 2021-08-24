while True:
    n, m = input().split()
    n = int(n)
    m = int(m)
    if n == 0 and m == 0:
        break

    v = input().split()
    for i in range(0, m):
        v[i] = int(v[i])

    b = [0] * (n+1)

    r = 0

    for i in v:
        b[i] += 1

    for i in range(1, n+1):
        if b[i] > 1:
            r += 1

    print(r)
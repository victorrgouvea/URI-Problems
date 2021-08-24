while True:
    p, n, c = map(int, input().split())
    if p == n == c == 0:
        break

    m = [0] * p
    nP = 0

    while n > 0:
        v = [int(x) for x in input().split()]
        for i in range(0, p):
            if v[i] == 1:
                m[i] += 1
                if m[i] == c:
                    nP += 1
            else:
                m[i] = 0
        n -= 1

    print(nP)
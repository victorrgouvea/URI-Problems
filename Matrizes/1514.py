while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    carac = 4
    mat = [None] * n
    for i in range(0, n):
        mat[i] = [int(i) for i in input().split()]

    for i in range(n):
        p = mat[i].count(1)
        if p == m:
            carac -= 1
            break

    prob = [0] * m
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                prob[j] += 1

    if prob.count(0) > 0:
        carac -= 1

    for i in range(m):
        if prob[i] == n:
            carac -= 1
            break

    for i in range(n):
        if 1 not in mat[i]:
            carac -= 1
            break

    print(carac)
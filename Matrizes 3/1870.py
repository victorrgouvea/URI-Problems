while True:
    l, c, p = map(int, input().split())
    if l == c == p == 0:
        break

    mat = [None] * l
    for i in range(l):
        mat[i] = [int(k) for k in input().split()]

    for i in range(l):
        forca = abs(mat[i][0] - mat[i][c-1])
        if mat[i][0] > mat[i][c-1]:
            p += forca
        elif mat[i][0] < mat[i][c-1]:
            p -= forca

while True:
    n = int(input())
    if n == 0:
        break

    mat = [0] * n
    for i in range(n):
        mat[i] = [0] * n

    for i in range(n):
        for j in range(n):
            potencia = i + j
            mat[i][j] = 2**potencia

    w = len(str(mat[n-1][n-1]))
    for i in range(n):
        print('{number:{width}d}'.format(width=w, number=(mat[i][0])), end='')
        for j in range(1, n):
            print(' {number:{width}d}'.format(width=w, number=(mat[i][j])), end='')
        print()
    print("")
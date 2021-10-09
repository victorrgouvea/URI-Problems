while True:
    l, c, p = map(int, input().split())
    if l == c == p == 0:
        break

    p -= 1
    b1 = 0
    b2 = 0
    boom = False
    mat = [None] * l
    for i in range(l):
        mat[i] = [int(k) for k in input().split()]

    for i in range(l):
        forca = abs(mat[i][0] - mat[i][c-1])
        pEntrada = p
        if mat[i][0] > mat[i][c-1]:
            p += forca
            for j in range(pEntrada, p+1):
                if mat[i][j] == 1:
                    b1 = i+1
                    b2 = j+1
                    boom = True
                    break
        elif mat[i][0] < mat[i][c-1]:
            p -= forca
            for j in range(p, pEntrada+1):
                if mat[i][j] == 1:
                    b1 = i+1
                    b2 = j+1
                    boom = True
                    break

    if boom:
        print("BOOM {} {}".format(b1,b2))
    else:
        print("OUT {}".format(p+1))
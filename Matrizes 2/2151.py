c = int(input())
p = 0

while c > 0:
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1

    mat = [None] * m
    for i in range(m):
        mat[i] = [int(k) for k in input().split()]

    for i in range(m):
        for j in range(n):
            distancia = max(abs(i-x),abs(j-y))
            if distancia > 8:
                mat[i][j] += 1
            else:
                mat[i][j] += (10-distancia)

    p += 1
    print("Parede {}:".format(p))
    for i in range(m):
        print("%d" % (mat[i][0]), end='')
        for j in range(1, n):
            print(" %d" % mat[i][j], end='')
        print()

    c -= 1
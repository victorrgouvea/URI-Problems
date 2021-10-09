while True:
    try:
        n = int(input())
        quadrado1 = n // 3

        mat = [0] * n
        for i in range(n):
            mat[i] = [0] * n

        for i in range(n):
            for j in range(n):
                if i == j:
                    mat[i][j] = 2
                elif i+j == (n-1):
                    mat[i][j] = 3

        for i in range(quadrado1, (n-quadrado1)):
            for j in range(quadrado1, (n-quadrado1)):
                mat[i][j] = 1

        meio = int((n-1) / 2)
        mat[meio][meio] = 4

        for i in range(n):
            for j in range(n):
                print("%d" % mat[i][j], end='')
            print()
        print("")

    except EOFError:
        break
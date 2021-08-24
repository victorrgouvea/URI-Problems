while True:
    try:
        n = int(input())

        mat = [0] * n
        for i in range(n):
            mat[i] = [0] * n

        for i in range(n):
            for j in range(n):
                if n >= 11 and 3 <= i <= 7 and 3 <= j <= 7:
                    mat[i][j] = 1
                else:
                    if i == j:
                        mat[i][j] = 2
                    elif i+j == (n-1):
                        mat[i][j] = 3

        meio = int((n-1) / 2)
        mat[meio][meio] = 4

        for i in range(n):
            for j in range(n):
                print("%d" % mat[i][j], end='')
            print()
        print("")

    except EOFError:
        break
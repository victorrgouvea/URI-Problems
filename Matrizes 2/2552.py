while True:
    try:
        n, m = map(int, input().split())

        #casas com pão de queijo
        mat = [None] * n
        for i in range(n):
            mat[i] = input().split()

        #resultado do tabuleiro final
        tabuleiro = [None] * n
        for i in range(n):
            tabuleiro[i] = [0] * m

        #analiso cada elemento e condiciono a ação a ser tomada
        for i in range(n):
            for j in range(m):
                if mat[i][j] == '1':
                    tabuleiro[i][j] = 9
                else:
                    if i-1 >= 0 and mat[i-1][j] == '1':
                        tabuleiro[i][j] += 1
                    if i+1 < n and mat[i+1][j] == '1':
                        tabuleiro[i][j] += 1
                    if j-1 >= 0 and mat[i][j-1] == '1':
                        tabuleiro[i][j] += 1
                    if j+1 < m and mat[i][j+1] == '1':
                        tabuleiro[i][j] += 1

        for i in range(n):
            for j in range(m):
                print("%d" % (tabuleiro[i][j]), end='')
            print()

    except EOFError:
        break
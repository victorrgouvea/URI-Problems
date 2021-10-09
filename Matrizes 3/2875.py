while True:
    try:
        m, n = map(int, input().split())

        mat = [None] * m
        for i in range(m):
            mat[i] = input().split()

        m -= 1
        n -= 1
        x = 0
        y = 0
        for i in range(m+1):
            for j in range(n+1):
                if mat[i][j] == 'X':
                    x = i
                    y = j
                    break

        instrucoes = []
        direcao = 'b' #baixo-b, cima-c, esquerda-e, direita-d
        while True:
            mat[x][y] = '2'
            proxX = '-1'
            proxY = '-1'

            #vizinho de cima
            vizI = x - 1
            vizJ = y
            if vizI >= 0 and mat[vizI][vizJ] == '0':
                proxX = vizI
                proxY = vizJ

                if direcao == 'e':
                    instrucoes.append('R')
                elif direcao == 'd':
                    instrucoes.append('L')

                instrucoes.append('F')
                direcao = 'c'

            #vizinho de baixo
            vizI = x + 1
            vizJ = y
            if vizI <= m and mat[vizI][vizJ] == '0':
                proxX = vizI
                proxY = vizJ

                if direcao == 'e':
                    instrucoes.append('L')
                elif direcao == 'd':
                    instrucoes.append('R')

                instrucoes.append('F')
                direcao = 'b'

            #vizinho da esquerda
            vizI = x
            vizJ = y - 1
            if vizJ >= 0 and mat[vizI][vizJ] == '0':
                proxX = vizI
                proxY = vizJ

                if direcao == 'c':
                    instrucoes.append('L')
                elif direcao == 'b':
                    instrucoes.append('R')

                instrucoes.append('F')
                direcao = 'e'

            #vizinho da direita
            vizI = x
            vizJ = y + 1
            if vizJ <= n and mat[vizI][vizJ] == '0':
                proxX = vizI
                proxY = vizJ

                if direcao == 'c':
                    instrucoes.append('R')
                elif direcao == 'b':
                    instrucoes.append('L')

                instrucoes.append('F')
                direcao = 'd'

            if proxX == '-1':
                instrucoes.append('E')
                for i in range(0, len(instrucoes)-1):
                    print("%s " % (instrucoes[i]), end='')
                print("%s" % (instrucoes[len(instrucoes)-1]))
                break
            else:
                x = proxX
                y = proxY

    except EOFError:
        break
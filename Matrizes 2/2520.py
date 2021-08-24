while True:
    try:
        n, m = map(int, input().split())
        cordPessoa = []
        cordPoke = []

        mat = [None] * n
        for i in range(n):
            mat[i] = input().split()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == '2':
                    cordPoke.append(i+1)
                    cordPoke.append(j+1)
                elif mat[i][j] == '1':
                    cordPessoa.append(i+1)
                    cordPessoa.append(j+1)

        menorTempo = (abs(cordPessoa[0]-cordPoke[0])) + (abs(cordPessoa[1]-cordPoke[1]))
        print(menorTempo)

    except EOFError:
        break
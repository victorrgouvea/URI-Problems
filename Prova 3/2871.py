while True:
    try:
        m, n = map(int, input().split())  #entrada das dimensões da matriz

        litros = 0  #aqui armazeno o total de litros que a lavoura irá produzir

        #Crio a matriz que representa a lavoura:
        mat = [None] * m
        for i in range(m):
            mat[i] = [int(x) for x in input().split()]

        #Percorro a matriz e somo no total de litros o quanto cada pé vai produzir
        for i in range(m):
            for j in range(n):
                litros += mat[i][j]

        sacas = litros // 60  #calculo o número de sacas que serão produzidas
        litros = litros % 60  #atualizo a variável "litros" para indicar o valor da sobra de café que não foi sufuciente para formar uma saca

        print("{} saca(s) e {} litro(s)".format(sacas, litros))  #imprimo os valores da produção da lavoura

    except EOFError:
        break
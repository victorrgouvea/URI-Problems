t = int(input())  #entrada do número de instâncias

while t > 0:
    n, l = map(int, input().split()) #entrada da dimensão das matrizes e do total de entradas não nulas

    #Crio a matriz soma:
    mat = [0] * (n+1)
    for i in range(n+1):
        mat[i] = [0] * (n+1)

    #Aqui leio os valores não nulos e suas coordenadas de cada umas das várias matrizes
    for i in range(l):
        p, k, c, v = map(int, input().split())
        mat[k][c] += v  #somo o valor na matriz soma na mesma coordenada da sua matriz original

    #Percorro a matriz soma a procura dos valores não nulos
    for i in range(n+1):
        for j in range(n+1):
            if mat[i][j] != 0:   #caso o valor seja diferente de 0, imprimo suas coordenadas e o próprio valor
                print("{} {} {}".format(i, j, mat[i][j]))

    #Aqui imprimo uma linha em branco somente entre duas instâncias
    if t > 1:
        print("")

    t -= 1
l, c = map(int, input().split())
a, b = map(int, input().split())

#ajuste para se referir a linha e coluna correta, ja que começa em 0
a -= 1
b -= 1

mat = [None] * l
for i in range(l):
    mat[i] = input().split()

while True:
    mat[a][b] = '2' #marco com 2 quem já foi checado
    proxA = '-1' #armazeno as coordenadas da próxima casa que o robo vai
    proxB = '-1'

    #vizinho de cima
    vizI = a - 1
    vizJ = b
    if vizI >= 0 and mat[vizI][vizJ] == '1': #pode ir para cima
        proxA = vizI
        proxB = vizJ

    #vizinho de baixo
    vizI = a + 1
    vizJ = b
    if vizI < l and mat[vizI][vizJ] == '1':
        proxA = vizI
        proxB = vizJ

    #vizinho da esquerda
    vizI = a
    vizJ = b - 1
    if vizJ >= 0 and mat[vizI][vizJ] == '1':
        proxA = vizI
        proxB = vizJ

    #vizinho da direita
    vizI = a
    vizJ = b + 1
    if vizJ < c and mat[vizI][vizJ] == '1':
        proxA = vizI
        proxB = vizJ

    #caso nenhum vizinho seja igual a 1:
    if proxA == '-1':
        print("{} {}".format(a+1,b+1)) #adiciono 1, já que descontei 1 em a e b para ficar nos padrões dos indices da matriz criada no código
        break
    else:
        a = proxA
        b = proxB
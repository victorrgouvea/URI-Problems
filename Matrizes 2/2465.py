n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1

#numero da camisa
mat = [None] * n
for i in range(n):
    mat[i] = [None] * n

#bandeira levantada ou não
alta = [None] * n
for i in range(n):
    alta[i] = [None] * n

for i in range(n):
    mat[i] = [int(k) for k in input().split()]
    for j in range(n):
        alta[i][j] = False #marco todas as bandeiras como baixas

bandeiras = 1 #ja somando a primeira coordenada
alta[x][y] = True #marco o primeiro aluno com a bandeira levantada
proxAluno = []
proxAluno.append((x,y)) #crio uma lista dos alunos que devem ser analisados

while proxAluno != []:
    (k,l) = proxAluno.pop(0) #retiro um aluno da lista

    #vizinho de cima
    vizK = k - 1
    vizL = l
    if vizK >= 0 and mat[vizK][vizL] >= mat[k][l] and alta[vizK][vizL] == False:
        bandeiras += 1
        alta[vizK][vizL] = True
        proxAluno.append((vizK, vizL))

    #vizinho de baixo
    vizK = k + 1
    vizL = l
    if vizK < n and mat[vizK][vizL] >= mat[k][l] and alta[vizK][vizL] == False:
        bandeiras += 1
        alta[vizK][vizL] = True
        proxAluno.append((vizK, vizL))

    #vizinho da esquerda
    vizK = k
    vizL = l - 1
    if vizL >= 0 and mat[vizK][vizL] >= mat[k][l] and alta[vizK][vizL] == False:
        bandeiras += 1
        alta[vizK][vizL] = True
        proxAluno.append((vizK, vizL))

    #vizinho da direita
    vizK = k
    vizL = l + 1
    if vizL < n and mat[vizK][vizL] >= mat[k][l] and alta[vizK][vizL] == False:
        bandeiras += 1
        alta[vizK][vizL] = True
        proxAluno.append((vizK, vizL))

print(bandeiras)
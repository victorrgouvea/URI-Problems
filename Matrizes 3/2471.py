n = int(input())

numeroOriginal = 0
mat = [None] * n
for i in range(n):
    mat[i] = [int(x) for x in input().split()]

#descobrindo a soma correta, a incorreta e a linha onde a soma é incorreta
somaCorreta = 0
somaIncorreta = 0
linhaIncorreta = 0
somasLinhas = [0] * n
for i in range(n):
    for j in range(n):
        somasLinhas[i] += mat[i][j]

for i in range(n):
    if somasLinhas.count(somasLinhas[i]) == n-1:
        somaCorreta = somasLinhas[i]
    elif somasLinhas.count(somasLinhas[i]) == 1:
        linhaIncorreta = i
        somaIncorreta = somasLinhas[i]

#descobrindo a coluna onde a soma é incorreta
somasColunas = [0] * n
colunaIncorreta = 0
for j in range(n):
    for i in range(n):
        somasColunas[j] += mat[i][j]

for i in range(n):
    if somasLinhas.count(somasColunas[i]) == 1:
        colunaIncorreta = i
        break

numeroColocado = mat[linhaIncorreta][colunaIncorreta]
numeroOriginal = abs(somaCorreta-somaIncorreta+numeroColocado)

print("{} {}".format(numeroOriginal, numeroColocado))
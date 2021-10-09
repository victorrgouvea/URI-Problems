n, m = map(int, input().split())

#matriz da fazenda de minhocas
maior = 0
mat = [None] * n
for i in range(n):
    mat[i] = [int(x) for x in input().split()]

#soma das linhas
for i in range(n):
    minhocasLinha = 0
    for j in range(m):
        minhocasLinha += mat[i][j]
    if minhocasLinha > maior:
        maior = minhocasLinha

#soma das colunas
for j in range(m):
    minhocasColuna = 0
    for i in range(n):
        minhocasColuna += mat[i][j]
    if minhocasColuna > maior:
        maior = minhocasColuna

print(maior)
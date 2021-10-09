n = int(input())  # Entrada do tamanho da floresta
especies = []  # Lista que armazena o número de cada espécie capturada

# Crio a matriz que representa a floresta
mat = [None] * n
for i in range(n):
    mat[i] = [int(x) for x in input().split()]

# Recebo cada coordenada visitada por Bino e subtraio 1 para adequar as coordenadas para a matriz criada acima
for i in range(n*2):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    # Adiciono o número da espécie na lista caso ainda não esteja lá
    if mat[x][y] not in especies:
        especies.append(mat[x][y])

print(len(especies))  # Imprimo a quantidade de elementos da lista "especies", que representa a quantidade de espécies diferentes coletadas
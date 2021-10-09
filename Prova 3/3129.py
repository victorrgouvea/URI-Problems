n = int(input())  #entrada do número de figurinhas
colecao = [0] * 301 #lista que representa a coleção inteira de figurinhas, onde cada valor representa a quantidade de figurinhas de cada número, representado pelo índice

#Aqui armazeno o número de figurinhas repetidas e diferentes
repetidas = 0
diferentes = 0

#Adiciono 1 na casa de índice igual ao número da figurinha, a fim de armazenar quantas figurinhas de cada número existem
for i in range(n):
    figurinha = int(input())
    colecao[figurinha] += 1

#Verifico quais figurinhas existem na coleção
for i in colecao:
    if i != 0:
        diferentes += 1  #para cada casa com uma ou mais figurinhas, adiociono 1 ao número de figurinhas diferentes
        if i > 1:
            repetidas += i-1  #caso exista mais de uma figurinha de algum número, adiociono a quantidade de figurinhas extras em "repetidos"

#Imprimo os valores de figurinhas diferentes e repetidas
print(diferentes)
print(repetidas)
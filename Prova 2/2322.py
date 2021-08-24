n = int(input())                  #Leitura do número de N de peças do quebra-cabeça
pecas = list(map(int, input().split())) #Aqui crio um vetor com as peças disponíveis e faço a transoformação para inteiro
pecasT = [0] * (n+1)    #Aqui crio um outro vetor para registrar a presença ou não das peças baseado no índice
pecaFaltando = 0        #Variável que armazena o número da peça que falta

for i in pecas:         #Aqui somo 1 no índice com o número da peça disponível. Sendo assim, teremos 0 no vetor "pecasT" apenas no índice que equivale ao número da peça que falta
    pecasT[i] += 1

for i in range(1, n+1): #Aqui procuramos pelo o elemento "0" no vetor "pecasT" e definimos a váriável pecaFaltando como o seu índice, que é o número da peça que falta
    if pecasT[i] == 0:
        pecaFaltando = i
        break

print(pecaFaltando)  #Impressão do número da peça que falta
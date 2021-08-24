sorteados = input().split()  #Vetor com os números sorteados entre 1 e 99
aposta = input().split()     #Vetor com os números apostados
acertos = 0      #Variável que representa o número de acertos

for i in aposta:        #Neste for verificamos cada número apostado e vemos se ele está entre os sorteados.
    if i in sorteados:  #Caso esteja, adicionamos 1 ao número de acertos
        acertos += 1

if acertos == 3:        #Daqui para baixo condicionamos o prêmio baseado no número de acertos da aposta e imprimimos o prêmio
    print("terno")

elif acertos == 4:
    print("quadra")

elif acertos == 5:
    print("quina")

elif acertos == 6:
    print("sena")

else:
    print("azar")
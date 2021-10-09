n = int(input())  #entrada do número de salas do corredor

corredor = [int(x) for x in input().split()]  #crio uma lista com as vidas de cada sala do corredor
maiorSoma = 0  #armazeno a maior soma de vidas que eu encontrar
soma = 0  #armazeno a soma atual que eu estiver operando

#Aqui faço as somas a partir da primeira sala:
for sala in corredor:
    soma += sala

    #caso essa soma de negativa, sei que ela não vai ser a maior, então recomeço a soma:
    if soma < 0:
        soma = 0

    #caso a soma que esteja sendo calculada seja maior que a considerada maior anteriormente, atualizo o valor de maior soma
    if soma > maiorSoma:
        maiorSoma = soma

print(maiorSoma)  #imprimo o valor da maior soma de vidas
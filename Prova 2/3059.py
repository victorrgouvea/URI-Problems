n, min, max = map(int, input().split())  #Entradas do número de elementos do vetor, do valor mínimo e do valor máximo
v = list(map(int, input().split()))   #Lista, com os números transformados para inteiros, dos valores a serem somados
pares = 0   #Variável que representa o total de pares cuja soma está no intervalo desejado
aux = 0   #Variável auxiliar, que vai aumentando de 1 em 1 para que dois valores não sejam comparados duas vezes no for abaixo

for i in v:                        #Nesses for's 1 valor será comparado com todos os outros da lista "v"
    for j in range(aux, n):
        if i != v[j] and min <= (i+v[j]) <= max:   #O valor não será somado com ele mesmo(parte do !=)
            pares += 1                             #E caso sua soma com outro valor esteja dentro do intervalo solicitado será somado 1 no total de pares

    aux += 1    #Aqui somamos 1 na variável auxiliar para garantir que o valor comparados anteriormente não seja comparado novamente

print(pares) #Impressão do total de pares que satisfazem a condição
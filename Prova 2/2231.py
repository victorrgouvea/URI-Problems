from math import trunc
t = 0   #Contador do número a ser impresso com o teste
while True:
    temp, inter = map(int, input().split())  #Entradas do total de medições feitas e do tamanho do intervalo desejado
    if temp == inter == 0:                   #Caso ambos os valores forem 0 o programa encerra
        break

    sensor = []     #Aqui armazenamos as temperaturas medidas pelo sensor
    medias = []     #Aqui armazenamos as médias de cada intervalo
    aux = 0      #Variáveis que irão dizer a posição do elemento a ser somado ou subtraído do total que será calculada a média
    aux2 = inter

    for i in range(temp):
        sensor.append(int(input()))    #Adição de cada medição do sensor ao vetor que as armazena

    total = 0   #Variável que vai indicar o total a ser usado para o cálculo da média
    for j in range(inter):   #Aqui faremos a adição dos valores da primeira média em total
        total += sensor[j]
    medias.append(trunc(total / inter))  #Cálculo da primeira média, que é adiocionada ao vetor "medias"


    for i in range(temp-inter):  #Aqui faremos o cálculo das demais médias e as colocaremos no vetor que as armazena
        total -= sensor[aux]   #Para calcular as novas médias, subtraímos o primeiro e o último valor que foram somados na média anterior
        total += sensor[aux2]
        medias.append(trunc(total / inter))
        aux += 1   #Aqui somamos 1 as variáveis auxiliares, que irão identificar os próximos elementos a serem somados ou subtraídos do total, para o cálculo da próxima média
        aux2 += 1

    mediamax = max(medias) #Aqui identificamos qual é a maior e a menor média da lista "medias"
    mediamin = min(medias)

    t += 1   #Somamos 1 em "t" para que a impressão do teste fique correta
    print("Teste {}".format(t))   #Impressão da linha que indica o teste
    print("{} {}".format(mediamin, mediamax))   #Impressão da menor e maior média
    print("")   #Impressão da linha em branco exigida pelo exercício
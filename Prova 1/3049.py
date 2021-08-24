b = int(input())                 #entradas dos valores das distâncias dos cortes
t = int(input())

pF = ((b+t)*70) / 2              #cálculo da área do pedaço de Felix (fórmula de área de trapézio)
pM = (((160-b)+(160-t))*70) / 2  #cálculo da área do pedaço de Marzia (fórmula de área de trapézio)

if pF > pM:        #aqui condicionamos quem fica com o pedaço que vale 100 reais baseado na maior área ou se o valor é perdido caso as áreas sejam iguais
    print("1")

elif pM > pF:
    print("2")

else:
    print("0")
o = input()  #entrada indicando a operação

#Crio a matriz 12x12:
m = [None] * 12
for i in range(0, 12):
    m[i] = [None] * 12

#Adiociono os valores que compõem a matriz:
for i in range(0, 12):
    for j in range(0, 12):
        m[i][j] = float(input())

total = 0  # variável que armazena a soma total dos valores da área inferior

#Aqui percorro todas as casas da área inferior da matriz, somando os valores na variável "total"
for i in range(7, 12):
    for j in range(12-i, i):
        total += m[i][j]

if o == 'S':
    print("%.1f" % total)  # caso a operação solicitada seja a soma, apenas imprimimos o valor de "total"
else:
    print("%.1f" % (total / 30))  # caso a operação seja a média, imprimimos o total dividido pelo número de casas da área inferior, que é 30
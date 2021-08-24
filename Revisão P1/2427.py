l = int(input()) #lado do quadrado
n = 0           #n vezes que o quadrado é dividido

while l >= 2:   #enquanto o l for maior ou igual a 2, dividi-se o lado pela metade e as n vezes que ele é dividido são armazenadas
    l = l/2
    n += 1

print("{}".format(4**n)) #como para cada n o quadrado é dividido em quatro parte, 4^n dará o número de pedaços
t = 0
while True:
    n = int(input())
    t += 1
    if n == 0:
        break

    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    n -= 1
    somaAcumulada = 0
    m = 1
    s1 = x1 - x2

    while n > 0:
        x, y = input().split()
        x = int(x)
        y = int(y)
        m += 1

        s2 = x - y


        n -= 1


'''
9
2 2
0 5
6 2
1 4
0 0
5 1
1 5
6 2
0 5

t = 0
while True:
leia(n)

t += 1

if n == 0: break

maior = 0
maiorIniPeriodo = 1
maiorFimPeriodo = 1

somaAcumulada = 0
tempIniPeriodo = 1
for i = 1...n:
    leia(x,y)
    dif = x - y
    
    somaAcumulada += dif
    
    if somaAcumulada > maior:
        maior = somaAcumulada
        maiorFimPeriodo = i
        maiorIniPeriodo = tempIniPeriodo
    elif somaAcumulada == maior:
        if (i - tempIniPeriodo) > (maiorFimPeriodo - maiorIniPeriodo):
        maiorFimPeriodo = i
        maiorIniPeriodo = tempIniPeriodo
    elif somaAcumulada < 0:
        somaAcumulada = 0
        tempIniPeriodo = i + 1
        
if maior <= 0 :
    imprime(nenhum)
else: 
    imprime(maiorIniPeriodo, maiorFimPeriodo)
'''


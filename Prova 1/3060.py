v = int(input())                    #entradas do valor e do número de parcelas, respectivamente
p = int(input())

r = v % p                           #cálculo do resto da divisão do valor em parcelas
vP = v // p                         #cálculo arredondado do valor de cada parcela

if r == 0:                          #caso o resto da divisão dê 0, imprimi-se o mesmo valor para todas as parcelas
    for _ in range(1, p+1):
        print("{}".format(vP))

else:                               #caso o resto da divisão seja diferente de 0, subtrai-se 1 do valor do resto e soma-se esse valor nas parcelas até que o valor do resto seja zerado.
    for _ in range(1, p+1):
        if r > 0:
            r -= 1
            print("{}".format(vP+1))
        else:
            print("{}".format(vP))
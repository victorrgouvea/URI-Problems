n = int(input())             #entrada do número de valores citados na reunião
s = 0                        #variável que representa o saldo total da universidade

while n > 0:                 #aqui serão recebidos os valores de verba ou gastos da universidades, sendo t a identificação entre verba e gasto e c os seus valores
    t, c = input().split()
    t = str(t)
    c = int(c)

    if t == "G":             #caso t identifique um gasto, esse valor é subtraído do saldo total
        s -= c

    elif t == "V":           #caso t identifique uma verba, esse valor é somado ao saldo total
        s += c

    n -= 1

if s >= 0:                                    #caso o saldo seja maior ou igual a zero, a universidade conseguirá cobrir seus gastos até o final do ano e a greve acaba
    print("A greve vai parar.")

else:
    print("NAO VAI TER CORTE, VAI TER LUTA!") #caso o saldo seja menor que zero, a universidade não conseguirá cobrir seus gastos e a greve continua
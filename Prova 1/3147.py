h, e, a, o, w, x = input().split()       #entradas dos números de exército de cada raça
h = int(h)
e = int(e)
a = int(a)
o = int(o)
w = int(w)
x = int(x)

lB = h + e + a             #soma do exército do lado do bem
lM = o + w                 #soma do exército do lado do mal

if lB <= lM:               #caso o exército do lado do bem perca, deve-se somar o exército de águias ao lado do bem
    lB += x

if lB >= lM:                          #aqui condicionamos as impressões do vencedor baseado em que lado tem o maior número de soldados(empate conta como vitória para o lado do bem por conta de Bilbo)
    print("Middle-earth is safe.")

else:
    print("Sauron has returned.")
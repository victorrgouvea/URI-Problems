#Entrada das coordenadas dos vértices do terreno A:
aX1, aY1 = map(int, input().split())
aX2, aY2 = map(int, input().split())
aX3, aY3 = map(int, input().split())
aX4, aY4 = map(int, input().split())

#Entrada das coordenadas dos vértices do terreno B:
bX1, bY1 = map(int, input().split())
bX2, bY2 = map(int, input().split())
bX3, bY3 = map(int, input().split())
bX4, bY4 = map(int, input().split())

#Aqui utilizo a Regra do Agrimensor para calcular a área dos dois terrenos
#OBS: o cálculo dentro do "abs" representa o determinante da matriz das coordenadas do terreno
areaA = abs((aX1*aY2)+(aX2*aY3)+(aX3*aY4)+(aX4*aY1)-(aX2*aY1)-(aX3*aY2)-(aX4*aY3)-(aX1*aY4)) / 2
areaB = abs((bX1*bY2)+(bX2*bY3)+(bX3*bY4)+(bX4*bY1)-(bX2*bY1)-(bX3*bY2)-(bX4*bY3)-(bX1*bY4)) / 2

#Daqui para baixo vejo qual terreno tem a maior área e imprimo esse resultado
if areaA > areaB:
    print("terreno A")
else:
    print("terreno B")
from math import sqrt
n = int(input())

while n > 0:
    x1, y1, x2, y2, x3, y3 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    y1 = int(y1)
    y2 = int(y2)
    y3 = int(y3)

    l1 = sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)       #usando a fórmula de distância entre dois pontos de GA para achar a medida dos lados
    l2 = sqrt(abs(x3 - x2) ** 2 + abs(y3 - y2) ** 2)
    l3 = sqrt(abs(x1 - x3) ** 2 + abs(y1 - y3) ** 2)

    p = (l1 + l2 + l3) / 2                                 #Cálculo do semi-perímetro para utilziar no teorema abaixo

    a = sqrt(p * (p - l1) * (p - l2) * (p - l3))           #usando o teorema de herão para calcular a área apenas pelas medidas dos lados do triangulo

    print("{:.3f}".format(a))

    n -= 1

    #d = abs((x1 * y2) + (x2 * y3) + (x3 * y1) - (x2 * x1) - (x3 * y2) - (x1 * y3))
    #a = d / 2
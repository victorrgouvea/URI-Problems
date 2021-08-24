a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

aT = (a*c) / 2
aC = 3.14159*(c**2)
aTp = ((a + b) * c) / 2
aQ = b**2
aR = a*b

print("TRIANGULO: %.3f" % aT)
print("CIRCULO: %.3f" % aC)
print("TRAPEZIO: %.3f" % aTp)
print("QUADRADO: %.3f" % aQ)
print("RETANGULO: %.3f" % aR)


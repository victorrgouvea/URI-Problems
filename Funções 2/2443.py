def mdc(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


a, b, c, d = map(int, input().split())
cima = (a*d) + (c*b)
baixo = b*d

simplificar = mdc(cima, baixo)

print("{} {}".format(int(cima/simplificar), int(baixo/simplificar)))
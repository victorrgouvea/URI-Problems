def pit(x, y, z):
    m = mdc(mdc(x, y), z)
    if tripla(x, y, z):
        if m == 1:
                return print("tripla pitagorica primitiva")
        return print("tripla pitagorica")
    return print("tripla")


def mdc(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def tripla(x, y, z):
    if z**2 == (x**2 + y**2):
        return True
    return False


while True:
    try:
        lados = [int(x) for x in input().split()]
        lados.sort()
        x = lados[0]
        y = lados[1]
        z = lados[2]
        pit(x, y, z)

    except EOFError:
        break
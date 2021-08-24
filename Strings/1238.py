n = int(input())

while n > 0:
    a, b = input().split()
    palavra = ''
    cont = 0

    while cont < len(a) and cont < len(b):
        palavra += a[cont] + b[cont]
        cont += 1

    if len(a) < len(b):
        palavra += b[cont:]

    elif len(a) > len(b):
        palavra += a[cont:]

    print(palavra)

    n -= 1
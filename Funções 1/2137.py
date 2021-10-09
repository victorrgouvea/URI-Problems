while True:
    try:
        n = int(input())

        lista = []
        for _ in range(n):
            lista.append(input())

        lista.sort()
        for cod in lista:
            print(cod)

    except EOFError:
        break
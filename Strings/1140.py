while True:
    frase = input()
    if frase == "*":
        break

    tautograma = True
    frase = frase.split(' ')
    lista1 = list(frase[0])
    letra = (lista1[0]).lower()
    for i in range(1, len(frase)):
        listaf = list(frase[i])
        letra2 = (listaf[0]).lower()
        if letra != letra2:
            tautograma = False
            break

    if tautograma:
        print("Y")
    else:
        print("N")
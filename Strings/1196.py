teclas = ['`', '1','2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
while True:
    try:
        frase = input()
        trad = ''
        for p in frase:
            if p == ' ':
                trad += ' '
            else:
                x = teclas.index(p)
                trad += teclas[x-1]

        print(trad)

    except EOFError:
        break
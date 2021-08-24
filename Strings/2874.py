while True:
    try:
        n = int(input())
        frase = ''
        while n > 0:
            bin = input()
            dec = int(bin, 2)
            letra = chr(dec)
            frase += letra

            n -= 1

        print(frase)

    except EOFError:
        break
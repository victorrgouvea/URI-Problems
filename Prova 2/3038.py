while True:
    try:
        frase = input()   #Entrada da frase criptografada

        frase = frase.replace('@', 'a')   #Daqui para baixo substituiremos os símbolos da tabela pela sua respectiva vogal
        frase = frase.replace('&', 'e')
        frase = frase.replace('!', 'i')
        frase = frase.replace('*', 'o')
        frase = frase.replace('#', 'u')

        print(frase)     #Impressão da frase descriptografada

    except EOFError:
        break
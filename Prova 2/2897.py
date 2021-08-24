while True:
    n = int(input())    #Entrada do número de comandos
    if n == 0:          #n = 0 indica o final da entrada
        break

    comandos = [int(i) for i in input().split()]   #Lista das posições dos comandos no histórico
    repetidos = []     #Lista que vai armazenar o histórico dos comandos novos
    pres = 0         #Variável que representa o total de vezes que a tecla deve ser pressionada
    adc = 0          #Variável armazena quantos comandos novos foram adiocionados ao histórico

    for i in comandos:
        if i in repetidos:                  #Caso um comando já tenha sido executado e esteja no histórico em "repetidos", o número de vezes que a tecla tem que ser pressionada é igual ao index daquele valor em "repetidos" + 1
            pres += repetidos.index(i) + 1
        else:                               #Caso contrário, o número de vezes que a tecla deve ser pressionada vai ser igual a sua posição dada na entrada mais o número de comandos adiocionados ao histórico
            pres += i + adc
        repetidos.insert(0, i)    #Aqui adiciono cada comando a lista que armazena os comandos novos
        adc += 1      #Aqui adiciono 1 para cada comando novo armazenado

    print(pres)  #Impressão do número de vezes que a tecla deve ser pressionada
# Crio uma lista com os dígitos a serem verificados
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    try:
        n = input()  # Entrada do número
        counts = []  # Lista que armazena a quantidade de vezes que cada dígito aparece no número

        # Aqui verifico quantas vezes cada número da lista aparece no número informado
        # e adiciono esse valor na lista "counts"
        for i in numeros:
            counts.append(n.count(i))

        mais_freq = max(counts)  # Encontro o valor mais repetido

        # Caso esse valor seja único, apenas um número é o mais repetido
        # Então faço a impressão dele baseado no índice de "mais_freq"
        if counts.count(mais_freq) == 1:
            print(counts.index(mais_freq))

        # Caso tenham dois valores que mais de repetem, tenho que imprimir o com o maior índice
        # Para isso, percorro a lista de trás pra frente, e assim que encontro um valor igual a "mais_freq", imprimo seu índice
        else:
            for i in range(9, -1, -1):
                if counts[i] == mais_freq:
                    print(i)
                    break

    except EOFError:
        break
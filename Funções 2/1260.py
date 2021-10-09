n = int(input())
linha_vazia = input()
arvores = {}
total = 0
nomes = []

while True:
    try:
        a = input()
        if a == '':
            if nomes != []:
                nomes.sort()
                for nome in nomes:
                    print("{} {:.4f}".format(nome, ((arvores[nome]) / total) * 100))
            print("")
            arvores = {}
            total = 0
            nomes = []
        else:
            total += 1
            if a not in arvores:
                arvores[a] = 1
                nomes.append(a)
            else:
                arvores[a] += 1

    except EOFError:
        nomes.sort()
        for nome in nomes:
            print("{} {:.4f}".format(nome, ((arvores[nome]) / total) * 100))
        break
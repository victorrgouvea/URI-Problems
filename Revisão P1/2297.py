t = 0 #número de testes
while True:
    r = int(input())
    t += 1
    a = 0 #contador de figurinhas de ambos
    b = 0

    if r == 0:
        break
    else:
        while r > 0:               #quantas figurinhas cada um ganhou em cada rodada
            c, d = input().split()
            c = int(c)
            d = int(d)
            a += c                 #adicionando o saldo de cada um ao contador com as figurinhas da rodada
            b += d
            r -= 1

        print("Teste {}".format(t))  #imprimindo as respostas baseado em quem tem mais figurinhas
        if a > b:
            print("Aldo")
        elif b > a:
            print("Beto")
        print("")
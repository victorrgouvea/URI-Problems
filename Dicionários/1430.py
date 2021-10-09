notas = {"W" : 1, "H" : 1/2, "Q" : 1/4, "E" : 1/8, "S" : 1/16, "T" : 1/32, "X" : 1/64}

while True:

    corretos = 0

    comp = input().split("/")
    if comp == ["*"]:
        break

    for compasso in comp:
        c = list(compasso)
        duracao = 0

        for nota in c:
            duracao += notas[nota]

        if duracao == 1:
            corretos += 1

    print(corretos)
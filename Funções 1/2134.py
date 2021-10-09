t = 0
while True:
    try:
        dic = {}
        n = int(input())

        nome_r, nota_r = input().split()
        nota_r = int(nota_r)

        for i in range(1, n):
            nome, nota = input().split()
            nota = int(nota)

            if nota < nota_r:
                nota_r = nota
                nome_r = nome
            elif nota == nota_r:
                if nome > nome_r:
                    nota_r = nota
                    nome_r = nome

        t += 1
        print("Instancia {}".format(t))
        print(nome_r)
        print("")

    except EOFError:
        break
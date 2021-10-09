n = int(input())  # Entrada do número de casos

for _ in range(n):
    f = input()  # Entrada da frase
    p = input()  # Entrada da palavra

    posicoes = []  # Lista que armazena as posições onde a palavra a ser procurada está na frase
    posicao = 0  # Variável que armazena as posições onde eu encontro a palavra desejada na frase

    # Caso a frase começe com a palavra ou seja igual a ela, adicionamos a posição 0 na lista
    if f == p:
        posicoes.append(0)
    elif f.startswith(p + ' '):  # Adiciono o espaço para ter certeza que estou contando como uma palavra e não uma subpalavra
        posicoes.append(0)

    # Caso a frase termine com a palavra, adicionamos sua posição na lista
    if f.endswith(' ' + p):
        posicoes.append(len(f) - len(p))  # Para achar a posição subtraimos os comprimentos das duas strings, já que a posição é o primeiro digito da palavra

    # Aqui procuro a palavra na frase até não achar ela mais
    # (quando o comando find() não acha nada, ele retorna -1)
    while True:
        posicao = f.find(' ' + p + ' ', posicao + 1)  # Procuro pela palavra(entre dois espaços em branco para evitar de achar uma subpalavra) a partir da posição anterior

        # Caso a posição seja igual a -1, nenhuma palavra igual pode ser encontrada a partir da posição atual
        # Então, o loop é quebrado
        if posicao == -1:
            break

        # Caso a posição não seja -1, o loop não é quebrado e adiciono a posição encontrado na lista
        posicoes.append(posicao + 1)  # Adiciono 1 por conta do espaço em branco adicionado

    # Caso nenhuma posição tenha sido encontrada, imprimo "-1"
    if posicoes == []:
        print("-1")

    # Caso contrário, imprimo as posições encontradas
    else:
        print(posicoes[0], end='')
        if len(posicoes) > 1:
            for i in range(1, len(posicoes)):
                print(" %s" % posicoes[i], end='')
        print()
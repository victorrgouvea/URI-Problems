n, m = map(int, input().split()) #entradas das dimensões da matriz

onlyZero = False  #variável que define se as próximas colunas devem ser todas compostas por zero
escada = True  #variável que define se a matriz é ou não uma escada
numEsquerda = 0 #variável que armazena o índice do número mais a esquerda da linha que está sendo analisada
esqAnterior = 0 #variável que armazena o índice do número mais a esquerda da linha anterior

#Neste for analiso as linhas da matriz e verifico as condições para a matriz ser uma escada:
for i in range(n):
    linha = [int(x) for x in input().split()] #entrada da linha da matriz

    #caso as próximas linhas devam ser todos zeradas, checo essa exigência para a linha atual:
    if onlyZero:
        if linha != ([0]*m):
            escada = False  #caso a linha não seja inteiramente zerada, digo que a matriz não é uma escada e encerro o for
            break

    #caso a condição da linha de zeros ainda não seja exigida, checo as condições para ela ser uma escada
    else:

        #caso a linha atual seja inteiramente zerada, indico que essa condição é verdadeira a partir de agora
        if linha == [0]*m:
            onlyZero = True

        #caso a linha não seja inteira de zeros, checo as outras exigências
        else:

            #descubro qual o índice do elemento mais a esquerda e diferente de 0 da linha
            for coluna in range(m):
                if linha[coluna] > 0:
                    numEsquerda = coluna
                    break

            #aqui checo o caso de o índice do número mais a esquerda da linha anterior ser maior que o índice atual
            #caso isso acontecessa, o número diferente de zero mais a esquerda da linha atual estaria a esquerda do número
            #mais a esquerda diferente de zero da linha anterior, o que seria considerado uma irregularidade na escada,
            #já que se esse número está a esquerda do anterior, ele deveria ser 0
            if esqAnterior >= numEsquerda and i > 0:
                escada = False  #se esse caso acontecer, considero que a matriz não é uma escada e encerro o for
                break

            esqAnterior = numEsquerda #aqui defino o índice do número a esquerda atual como anterior para testar a próxima linha

#imprimo se a matriz é uma escada ou não baseado se é verdadeira ou falsa
if escada:
    print("S")
else:
    print("N")
n, m, c = map(int, input().split()) #entradas das dimensões da matriz e do espaço necessário entre os alunos

#Crio a matriz que corresponde a sala de aula:
mat = [0] * n
for i in range(n):
    mat[i] = [int(x) for x in input().split()]

#Aqui verifico quais colunas contém pelo menos um aluno fazendo a prova e adiciono o número dessas colunas em uma lista:
colunas = []
for i in range(m):
    for j in range(n):
        if mat[j][i] != 0:
            colunas.append(i)
            break

regras = True #variável que representa se as regras impostas pela professora estão sendo seguidas ou não

#Neste for faço a verificação das regras da professora para as colunas com prova:
for coluna in colunas:

    #Caso alguma regra já tenha sido quebrada, encerro o loop
    if not regras:
        break

    #Verificação dos elementos da coluna analisada
    for elem in range(n):

        #verifico se a próxima coluna(a direita da verificada) contém algum aluno com prova
        #para isso, verifico se o elemento a direita do analisado é diferente de zero
        index = coluna+1
        if index < m and mat[elem][index] != 0: #caso exista alguma prova na próxima coluna, digo que a regra foi quebrada e encerro o loop
            regras = False
            break

        #caso o elemento analisado seja 1(prova 1), verifico se existe alguma prova igual dentro da distância estabelecida pela professora
        if mat[elem][coluna] == 1:
            for k in range(elem+1, elem+c+1):
                if k < n and mat[k][coluna] == 1: #caso uma dessas provas seja a prova 1, digo que a regra foi quebrada e encero o loop
                    regras = False
                    break

        #executo o mesmo processo descrito acima, só que para o caso de o elemento analisado ser 2(prova 2)
        if mat[elem][coluna] == 2:
            for k in range(elem+1, elem+c+1):
                if k < n and mat[k][coluna] == 2: #caso uma dessas provas seja a prova 2, digo que a regra foi quebrada e encero o loop
                    regras = False
                    break

#Imprimo que a prova pode ser ou não aplicada dependendo se todas as regras estão sendo seguidas ou não
if regras:
    print("S")
else:
    print("N")
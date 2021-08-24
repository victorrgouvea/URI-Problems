a, b, c = input().split()          #entradas dos valores de cada ingrediente
a = int(a)
b = int(b)
c = int(c)

f = a // 2                         #aqui calculamos quantas receitas conseguimos fazer com cada ingrediente
o = b // 3
l = c // 5

if f == o and f == l and o == l:  #caso o número de receitas dos 3 ingredientes sejam iguais, o número de receitas de bolo vai ser igual a qualquer uma das variáveis(f escolhida nesse caso)
    print("{}".format(f))
elif f <= o and f <= l:           #caso o número de receitas dos ingredientes sejam diferentes, o menor(ou menores) número(s) vai/vão identificar o número de receitas de bolo que podem ser feitas
    print("{}".format(f))         #os 3 primeiros elif executam a lógica do comentário acima
elif o <= f and o <= l:
    print("{}".format(o))
elif l <= f and l <= o:
    print("{}".format(l))
elif f == 0 or o == 0 or l == 0:  #caso o número de receitas de um dos ingredientes seja 0, significa que nenhuma receita de bolo pode ser feita
    print("0")
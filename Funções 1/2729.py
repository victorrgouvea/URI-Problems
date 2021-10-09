def filtrar_lista(v):
    for i in v:
        if i not in lista_att:
            lista_att.append(i)


n = int(input())
for _ in range(n):
    lista = input().split()
    lista_att = []
    filtrar_lista(lista)
    lista_att.sort()
    print(lista_att[0],end='')
    for prod in range(1, len(lista_att)):
        print(" %s" % lista_att[prod], end='')
    print()
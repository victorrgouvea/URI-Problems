while True:
    n = int(input())
    if n == 0:
        break

    v = input().split()
    for i in range(0, n):
        v[i] = int(v[i])
    vO = sorted(v, reverse=True)

    for i in range(0, n):
        if vO[1] == v[i]:
            sus = i + 1
            print(sus)

'''
lista ordem decrescente
lista ordem crescente:
lista.sort() ou ordenada = sorted(lista)
'''
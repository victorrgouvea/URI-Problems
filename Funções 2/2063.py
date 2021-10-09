def mdc(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def mmc(a, b):
    cima = a*b
    baixo = mdc(a, b)
    return cima/baixo


n = int(input())
buracos = [int(x) for x in input().split()]
tempos = []

for i in range(n):
    tempo = 1
    buraco = buracos[i]
    while buraco != (i+1):
        buraco = buracos[buraco-1]
        tempo += 1

    tempos.append(tempo)

menor = mmc(tempos[0], tempos[1])
for t in range(2, n):
    menor = mmc(menor, tempos[t])

print(int(menor))
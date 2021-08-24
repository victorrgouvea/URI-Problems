comp, gotas = map(int, input().split())
posicoes = [int(i) for i in input().split()]

fita1 = [0] * (comp+2)
fita1[0] = 1
fita1[comp-1] = 1

dias = 0

for i in posicoes:
    fita1[i] += 1

fita2 = fita1.copy()

while 0 in fita1:
    for i in range(1, comp+1):
        if fita1[i] == 1:
            a = i-1
            b = i+1
            fita2[a] = 1
            fita2[b] = 1
    dias += 1

    fita1 = fita2.copy()

print(dias)
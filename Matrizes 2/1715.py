n, m = map(int, input().split())

desempenho = []
golsEmTodas = 0
for i in range(n):
    desempenho.append([int(i) for i in input().split()])

for i in range(n):
    if 0 not in desempenho[i]:
        golsEmTodas += 1

print(golsEmTodas)
n = input()
n = int(n, 2)

m = int(input())
divisores = []
for i in range(m):
    d = int(input())
    if (n % d) == 0:
        divisores.append(d)

if divisores == []:
    print("Nenhum")
else:
    divisores.sort()
    print(divisores[0], end='')
    for i in range(1, len(divisores)):
        print(" %d" % divisores[i], end='')
    print()
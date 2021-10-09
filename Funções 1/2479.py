n = int(input())
criancas = []
sim = 0
nao = 0

for i in range(n):
    s, n = input().split()

    if s == '+':
        sim += 1
    else:
        nao += 1

    criancas.append(n)

criancas.sort()
for nome in criancas:
    print(nome)
print("Se comportaram: {} | Nao se comportaram: {}".format(sim, nao))
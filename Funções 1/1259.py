def add_list(x):
    if (x % 2) == 0:
        pares.append(x)
    else:
        impares.append(x)


pares = []
impares = []

n = int(input())
for _ in range(n):
    a = int(input())
    add_list(a)

pares.sort()
impares.sort(reverse=True)

for num in pares:
    print(num)

for num in impares:
    print(num)
l, n = map(int, input().split())
irg = []
vogal = ['a', 'e', 'i', 'o', 'u']
term = ["o", "s", "x", "ch", "sh"]

for i in range(0, l):
    v = input().split()
    irg.append(v[0])
    irg.append(v[1])

while n > 0:
    palavra = input()
    count = True
    for i in range(0, len(irg)):
        if irg[i] == palavra:
            print(irg[i+1])
            count = False
            break

    if count:

        if palavra[len(palavra)-1] == "y" and palavra[(len(palavra)-2)] not in vogal:
            print(palavra.replace("y", "ies"))

        elif palavra[len(palavra)-1] in term:
            print(palavra + 'es')

        elif (palavra[len(palavra)-2] + palavra[len(palavra)-1]) in term:
            print(palavra + 'es')

        else:
            print(palavra + 's')

    n -= 1
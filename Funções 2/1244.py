n = int(input())

for i in range(n):
    palavras = input().split()
    palavras.sort(key=len, reverse=True)

    print(palavras[0], end='')
    for j in range(1, len(palavras)):
        print(" %s" % palavras[j], end='')
    print()
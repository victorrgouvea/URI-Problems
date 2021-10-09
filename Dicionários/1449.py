t = int(input())

for _ in range(t):

    dic = {}
    m, n = map(int, input().split())

    for i in range(m):
        j = input()
        p = input()
        dic[j] = p

    for i in range(n):
        frase = input().split()
        for p in range(len(frase)):
            if frase[p] in dic:
                frase[p] = dic[frase[p]]

        frase = ' '.join(frase)
        print(frase)

    print("")
while True:
    dic = {}
    dif = 0

    n = int(input())
    if n == 0:
        break

    for _ in range(n):
        nome, ass = input().split()
        dic[nome] = ass

    m = int(input())
    for _ in range(m):
        d = 0
        nome, ass = input().split()

        for i in range(len(ass)):
            if ass[i] != (dic[nome])[i]:
                d += 1

        if d > 1:
            dif += 1

    print(dif)
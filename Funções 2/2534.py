while True:
    try:
        n, q = map(int, input().split())

        notas = []
        for i in range(n):
            notas.append(int(input()))

        notas.sort(reverse=True)
        for i in range(q):
            print(notas[(int(input()))-1])

    except EOFError:
        break
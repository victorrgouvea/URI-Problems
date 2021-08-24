while True:
    try:
        n, r = input().split()
        n = int(n)
        r = int(r)
        v = input().split()
        x = 0
        for i in range(0, r):
            v[i] = int(v[i])

        m = [0] * (n+1)
        m[0] = 1

        for i in v:
            m[i] = 1

        if 0 in m:
            for i in range(1, len(m)):
                if m[i] == 0:
                    print("%d " % i, end='')
            print("")
        else:
            print("*")

    except EOFError:
        break
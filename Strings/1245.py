while True:
    try:
        n = int(input())
        count = 0
        d = []
        e = []
        while n > 0:
            m, l = input().split()
            m = int(m)
            l = str(l)

            if l == "D":
                d.append(m)
            else:
                e.append(m)

            n -= 1

        for s in d:
            if s in e:
                count += 1
                e.remove(s)

        print(count)

    except EOFError:
        break
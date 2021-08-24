t = [31,29,31,30,31,30,31,31,30,31,30,31]
while True:
    try:
        m, d = input().split()
        m = int(m)
        d = int(d)
        i = 0

        if m == 12 and d == 25:
            print("E natal!")
        elif m == 12 and d == 24:
            print("E vespera de natal!")
        elif m == 12 and d > 25:
            print("Ja passou!")
        else:
            for x in range(m-1, len(t)):
                i += t[x]
            i -= d
            i -= 6
            print("Faltam {} dias para o natal!".format(i))

    except:
        break
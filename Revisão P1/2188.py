t = 0
while True:
    n = int(input())
    t += 1
    if n == 0:
        break
    else:
        m = n-1
        xx, yy, uu, vv = input().split()
        xx = int(xx)
        yy = int(yy)
        uu = int(uu)
        vv = int(vv)
        while m > 0:
            x, y, u, v = input().split()
            x = int(x)
            y = int(y)
            u = int(u)
            v = int(v)

            if xx < x:
                xx = x
            if yy > y:
                yy = y
            if uu > u:
                uu = u
            if vv < v:
                vv = v

            m -= 1

        if xx > uu and yy < vv:
            print("Teste {}".format(t))
            print("nenhum")
            print("")
        elif yy == y and vv == v and xx != x and uu != u:
            print("Teste {}".format(t))
            print("nenhum")
            print("")
        elif yy != y and vv != v and xx == x and uu == u:
            print("Teste {}".format(t))
            print("nenhum")
            print("")
        else:
            print("Teste {}".format(t))
            print("{} {} {} {}".format(xx, yy, uu, vv))
            print("")
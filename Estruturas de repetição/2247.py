t = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        t += 1
        d = 0
        print("Teste {}".format(t))
        while n != 0:
            j, z = input().split()
            j = int(j)
            z = int(z)
            d += j - z
            print("{}".format(d))
            n -= 1
        print("")
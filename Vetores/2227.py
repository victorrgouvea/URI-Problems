t = 0
while True:
    a, v = input().split()
    a = int(a)
    v = int(v)
    if a == 0 and v == 0:
        break

    t += 1
    nV = [0] * (a+1)

    for i in range(0, v):
        x, y = input().split()
        x = int(x)
        y = int(y)

        nV[x] += 1
        nV[y] += 1

    m = max(nV)
    print("Teste {}".format(t))
    for i in range(0, len(nV)):
        if nV[i] == m:
            print("%d " % i, end='')
    print("")
    print("")

#print((nV.index(m) + 1))
'''    for i in range(0, len(nV)):
        if nV[i] == m:
            print("%d" % (i), end='')
            x = i
            break
    for i in range(x+1, len(nV)):
        if nV[i] == m:
            print(" %d" % (i), end='')'''
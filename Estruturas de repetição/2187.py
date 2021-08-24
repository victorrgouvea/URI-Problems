i = 0
j = 0
k = 0
l = 0
n = 0

while True:
    v = int(input())
    if v == 0:
        break

    if v >= 50:
        i += v // 50
        v -= i*50
    if v >= 10:
        j += v // 10
        v -= j*10
    if v >= 5:
        k += v // 5
        v -= k*5
    if v >= 1:
        l += v

    n += 1

    print("Teste {}".format(n))
    print("{} {} {} {}".format(i, j, k, l))
    print("")

    i = 0
    j = 0
    k = 0
    l = 0
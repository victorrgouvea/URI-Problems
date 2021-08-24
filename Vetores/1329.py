while True:
    n = int(input())
    if n == 0:
        break
    v = input().split()
    m = 0
    j = 0
    for i in range(0, n):
        v[i] = int(v[i])

    for i in range(0, n):
        if v[i] == 0:
            m += 1
        else:
            j += 1

    print("Mary won {} times and John won {} times".format(m, j))
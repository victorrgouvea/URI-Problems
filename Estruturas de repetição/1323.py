while True:
    n = int(input())
    q = 0
    if n == 0:
        break

    for x in range(n, 0, -1):
        q += x**2

    print("{}".format(q))
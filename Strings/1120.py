while True:
    d, n = input().split()
    if d == n == "0":
        break

    n = '0' + n
    v = int(n.replace(d, ''))

    print(v)
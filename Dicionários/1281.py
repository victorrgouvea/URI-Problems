n = int(input())

for _ in range(n):

    feira = {}
    total = 0

    m = int(input())
    for i in range(m):
        p, v = input().split()
        v = float(v)
        feira[p] = v

    p = int(input())
    for i in range(p):
        p, q = input().split()
        q = int(q)
        total += feira[p] * q

    print("R$ {:.2f}".format(total))
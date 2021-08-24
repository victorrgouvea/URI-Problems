while True:
    n = int(input())
    l = 0
    if n == 0:
        break

    for i in range(0, n):
        c, v = map(int, input().split())
        q = v // 2

        if q > 0:
            l += q

    print(l//2)
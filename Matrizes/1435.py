while True:
    n = int(input())
    if n == 0:
        break

    m = [None] * n
    for i in range(0, n):
        m[i] = [None] * n

    for i in range(n):
        for j in range(n):
            m[i][j] = min(i+1,n-i,j+1,n-j)

    for i in range(n):
        print("%3d" % m[i][j], end='')
        for j in range(1, n):
            print(" %3d" % m[i][j], end='')
        print()
    print()
while True:
    n = int(input())
    if n == 0:
        break

    v = input().split()
    v.append(v[0])
    v.append(v[1])
    for i in range(0, n+2):
        v[i] = int(v[i])

    min = 0
    max = 0
    p = 0

    for i in range(1, n+2):
        if v[i] < v[i-1]:
            if max == 1:
                p += 1
                min = 1
                max = 0
            else:
                min = 1

        elif v[i] > v[i-1]:
            if min == 1:
                p += 1
                min = 0
                max = 1
            else:
                max = 1


    print(p)
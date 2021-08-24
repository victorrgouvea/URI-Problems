q = ["A", "B", "C", "D", "E"]
while True:
    n = int(input())
    if n == 0:
        break

    while n > 0:
        v = input().split()
        r = 0
        for i in range(0, len(v)):
            v[i] = int(v[i])
        for i in range(0, len(v)):
            if v[i] == 0 or v[i] <= 127:
                r += 1
        if r > 1 or r == 0:
            print("*")
        else:
            for i in range(0, len(v)):
                if v[i] == 0 or v[i] <= 127:
                    print(q[i])

        n -= 1
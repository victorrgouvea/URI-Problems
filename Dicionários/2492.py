while True:
    t = int(input())
    if t == 0:
        break

    x = []
    y = []
    inver = True

    for i in range(t):
        a, s, b = input().split()
        x.append(a)
        y.append(b)

    for i in range(t):

        if x.count(x[i]) > 1:
            inver = False
            print("Not a function.")
            break

    if inver:
        for i in range(t):

            if y.count(y[i]) > 1:
                inver = False
                print("Not invertible.")
                break

    if inver:
        print("Invertible.")
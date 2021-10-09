while True:
    a, d = map(int, input().split())
    if a == d == 0:
        break

    distA = [int(x) for x in input().split()]
    distD = [int(x) for x in input().split()]
    impedido = False

    distD.sort()
    for j in distA:
        if j < distD[1]:
            impedido = True
            break

    if impedido:
        print("Y")
    else:
        print("N")
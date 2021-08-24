t = 0
while True:
    n = int(input())
    if n == -1:
        break

    else:
        r = (1+(2**n))*(1+(2**n))

    t += 1
    print("Teste {}".format(t))
    print("{}".format(r))
    print("")
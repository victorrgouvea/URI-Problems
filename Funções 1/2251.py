t = 0
while True:
    n = int(input())
    if n == 0:
        break

    movimentos = (2**n) - 1  # relação de recorrência

    t += 1
    print("Teste {}".format(t))
    print(movimentos)
    print("")
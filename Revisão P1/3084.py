while True:
    try:
        h, m = input().split()   #entrada dos valores dos angulos
        h = int(h)
        m = int(m)

        if h == 360:             #no caso de ser 360º, no relógio é o mesmo que 0º, pois ambos devem ser 0
            h = 0                #então dizemos que, se for 360 também vale como 0
        if m == 360:
            m = 0

        hR = int(h / 30)         #aqui fazemos as operações para transformar de grau para hora e para minuto
        mR = int(m / 6)

        if hR < 10 and mR >= 10:              #aqui condinamos que, quando um dos números for menor que 10, deve-se adicionar um "0" ao texto de saída para adequar ao que a questão pede
            print("0{}:{}".format(hR, mR))
        elif mR < 10 and hR >= 10:
            print("{}:0{}".format(hR, mR))
        elif hR < 10 and mR < 10:
            print("0{}:0{}".format(hR, mR))
        else:
            print("{}:{}".format(hR, mR))

    except EOFError:
        break
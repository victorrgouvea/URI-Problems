while True:
    try:
        horas, minutos = list(map(int, input().split(":")))
        horas = bin(horas).replace('0b', '')
        minutos = bin(minutos).replace('0b', '')

        horabin = []
        minbin = []

        for i in range(0, len(horas)):
            if horas[i] == '1':
                horabin.insert(i, 'o')
            else:
                horabin.insert(i, ' ')

        while len(horabin) < 4:
            horabin.insert(0, ' ')

        for i in range(0, len(minutos)):
            if minutos[i] == '1':
                minbin.insert(i, 'o')
            else:
                minbin.insert(i, ' ')

        while len(minbin) < 6:
            minbin.insert(0, ' ')

        print(' ____________________________________________')
        print('|                                            |')
        print('|    ____________________________________    |_')
        print('|   |                                    |   |_)')
        print('|   |   8         4         2         1  |   |')
        print('|   |                                    |   |')
        print('|   |   {}         {}         {}         {}  |   |'.format(horabin[0], horabin[1], horabin[2], horabin[3]))
        print('|   |                                    |   |')
        print('|   |                                    |   |')
        print('|   |   {}     {}     {}     {}     {}     {}  |   |'.format(minbin[0], minbin[1], minbin[2], minbin[3], minbin[4], minbin[5]))
        print('|   |                                    |   |')
        print('|   |   32    16    8     4     2     1  |   |_')
        print('|   |____________________________________|   |_)')
        print('|                                            |')
        print('|____________________________________________|')
        print('')

    except EOFError:
        break
n = int(input())
k = 0

while n > 0:
    k += 1
    sudoku = []
    for i in range(0, 9):
        sudoku.append([int(i) for i in input().split()])

    original = True
    mat3 = [0] * 10
    linha = [0] * 10
    coluna = [0] * 10
    for i in range(0, 9):
        for j in range(0, 9):
            linha[(sudoku[i][j])] += 1
        if linha.count(i+1) != 9:
            original = False
            break

    for i in range(0, 9):
        for j in range(0, 9):
            coluna[(sudoku[j][i])] += 1
        if coluna.count(i+1) != 9:
            original = False
            break

    for i in range(0, 3):
        for j in range(0, 3):
            mat3[sudoku[i][j]] += 1
    if mat3.count(1) != 9:
        original = False

    for i in range(3, 6):
        for j in range(0, 3):
            mat3[sudoku[i][j]] += 1
    if mat3.count(2) != 9:
        original = False

    for i in range(6, 9):
        for j in range(0, 3):
            mat3[sudoku[i][j]] += 1
    if mat3.count(3) != 9:
        original = False

    for i in range(0, 3):
        for j in range(3, 6):
            mat3[sudoku[i][j]] += 1
    if mat3.count(4) != 9:
        original = False

    for i in range(3, 6):
        for j in range(3, 6):
            mat3[sudoku[i][j]] += 1
    if mat3.count(5) != 9:
        original = False

    for i in range(6, 9):
        for j in range(3, 6):
            mat3[sudoku[i][j]] += 1
    if mat3.count(6) != 9:
        original = False

    for i in range(0, 3):
        for j in range(6, 9):
            mat3[sudoku[i][j]] += 1
    if mat3.count(7) != 9:
        original = False

    for i in range(3, 6):
        for j in range(6, 9):
            mat3[sudoku[i][j]] += 1
    if mat3.count(8) != 9:
        original = False

    for i in range(6, 9):
        for j in range(6, 9):
            mat3[sudoku[i][j]] += 1
    if mat3.count(9) != 9:
        original = False

    if original:
        print("Instancia {}".format(k))
        print("SIM")
        print("")

    else:
        print("Instancia {}".format(k))
        print("NAO")
        print("")

    n -= 1
l, n = map(int, input().split())
D = l
E = l
F = l

while n > 0:
    opr = input().split()
    if opr[0] == "C" and opr[1] == "D":
        D -= int(opr[2])
    elif opr[0] == "C" and opr[1] == "E":
        E -= int(opr[2])
    elif opr[0] == "C" and opr[1] == "F":
        F -= int(opr[2])
    elif opr[0] == "V" and opr[1] == "D":
        D += int(opr[2])
    elif opr[0] == "V" and opr[1] == "E":
        E += int(opr[2])
    elif opr[0] == "V" and opr[1] == "F":
        F += int(opr[2])
    elif opr[0] == "A" and opr[1] == "D" and opr[2] == "E":
        D += int(opr[3])
        E -= int(opr[3])
    elif opr[0] == "A" and opr[1] == "E" and opr[2] == "D":
        E += int(opr[3])
        D -= int(opr[3])
    elif opr[0] == "A" and opr[1] == "D" and opr[2] == "F":
        D += int(opr[3])
        F -= int(opr[3])
    elif opr[0] == "A" and opr[1] == "F" and opr[2] == "D":
        F += int(opr[3])
        D -= int(opr[3])
    elif opr[0] == "A" and opr[1] == "F" and opr[2] == "E":
        F += int(opr[3])
        E -= int(opr[3])
    elif opr[0] == "A" and opr[1] == "E" and opr[2] == "F":
        E += int(opr[3])
        F -= int(opr[3])
    n -= 1

print("{} {} {}".format(D, E, F))
cV, cE, cS, fV, fE, fS = input().split()
cV = int(cV)
cE = int(cE)
cS = int(cS)
fV = int(fV)
fE = int(fE)
fS = int(fS)

pC = cV*3 + cE
pF = fV*3 + fE

if pC > pF:
    print("C")

elif pF > pC:
    print("F")

else:
    if cS > fS:
        print("C")

    elif fS > cS:
        print("F")

    else:
        print("=")
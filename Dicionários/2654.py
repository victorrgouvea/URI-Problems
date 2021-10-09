n = int(input())

godS, godP, godK, godM = input().split()
godP = int(godP)
godK = int(godK)
godM = int(godM)

for _ in range(1,n):
    s, p, k, m = input().split()
    p = int(p)
    k = int(k)
    m = int(m)

    troca = False
    if p > godP:
        troca = True
    elif p == godP:
        if k > godK:
            troca = True
        elif k == godK:
            if m < godM:
                troca = True
            elif m == godM and s < godS:
                troca = True

    if troca:
        godS = s
        godP = p
        godK = k
        godM = m

print(godS)
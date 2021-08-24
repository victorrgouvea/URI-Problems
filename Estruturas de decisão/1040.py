n1, n2 ,n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

m = (n1*2 + n2*3 + n3*4 + n4) / 10
print("Media: {:.1f}".format(m))

if m >= 7:
    print("Aluno aprovado.")

elif m < 5:
    print("Aluno reprovado.")

else:
    print("Aluno em exame.")

    nE = float(input())
    print("Nota do exame: {:.1f}".format(nE))

    mF = (m + nE) / 2

    if mF >= 5:
        print("Aluno aprovado.")

    else:
        print("Aluno reprovado.")

    print("Media final: {:.1f}".format(mF))
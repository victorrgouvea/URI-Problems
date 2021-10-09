n, m, s = map(int, input().split())
n += 1
m += 1

mat = [0] * (n)
for i in range(n):
    mat[i] = [0] * (m)

totalCampo = 0

for i in range(s):
    x, y, h = map(int, input().split())
    mat[x][y] += h
    totalCampo += h

#primeiro exército
primeiroExercito = 0
for i in range(n):
    for j in range(0+i, m):
        primeiroExercito += mat[i][j]

segundoExercito = totalCampo - primeiroExercito

print("{} {}".format(primeiroExercito, segundoExercito))
n = int(input())
v = input().split()

for i in range(0, n):
    v[i] = int(v[i])

mV = v[0]
p = 0

for i in range(1, n):
    if v[i] < mV:
        mV = v[i]
        p = i

print("Menor valor: {}".format(mV))
print("Posicao: {}".format(p))
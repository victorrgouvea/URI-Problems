l = int(input())
t = input()

m = [None] * 12
for i in range(0, 12):
    m[i] = [None] * 12

for i in range(0, 12):
    for j in range(0, 12):
        m[i][j] = float(input())

total = 0
for i in range(0, 12):
    total += m[l][i]

if t == 'S':
    print("%.1f" % total)
else:
    print("%.1f" % (total / 12))
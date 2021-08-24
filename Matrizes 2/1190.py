o = input()

m = [None] * 12
for i in range(0, 12):
    m[i] = [None] * 12

for i in range(0, 12):
    for j in range(0, 12):
        m[i][j] = float(input())

total = 0
for i in range(1, 6):
    for j in range(12-i, 12):
        total += m[i][j]

for i in range(6, 11):
    for j in range(i+1, 12):
        total += m[i][j]

if o == 'S':
    print("%.1f" % total)
else:
    print("%.1f" % (total / 30))
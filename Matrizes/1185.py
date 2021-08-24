o = input()

m = [None] * 12
for i in range(0, 12):
    m[i] = [None] * 12

for i in range(0, 12):
    for j in range(0, 12):
        m[i][j] = float(input())

total = 0
for i in range(0, 11):
    for j in range(0, 11-i):
        total += m[i][j]

if o == 'S':
    print("%.1f" % total)
else:
    print("%.1f" % (total / 66))
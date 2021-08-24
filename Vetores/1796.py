n = int(input())
v = input().split()
for i in range(0, n):
    v[i] = int(v[i])

f = 0
c = 0

for i in range(0, n):
    if v[i] == 0:
        f += 1
    else:
        c += 1

if f > c:
    print("Y")
else:
    print("N")
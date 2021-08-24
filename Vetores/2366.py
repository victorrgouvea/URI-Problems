n, m = input().split()
n = int(n)
m = int(m)
consegue = True

v = input().split()
v.append(42195)
for i in range(0, n+1):
    v[i] = int(v[i])

for i in range(0, n+1):
    x = int(v[i])
    y = int(v[i-1])
    if (x - y) > m:
        print("N")
        consegue = False
        break

if consegue:
    print("S")
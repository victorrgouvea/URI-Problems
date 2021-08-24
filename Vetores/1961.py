p, n = input().split()
p = int(p)
n = int(n)
j = True

v = input().split()
for i in range(0, n):
    v[i] = int(v[i])

for i in range(1, n):
    if abs(v[i-1] - v[i]) > p:
        print("GAME OVER")
        j = False
        break

if j:
    print("YOU WIN")
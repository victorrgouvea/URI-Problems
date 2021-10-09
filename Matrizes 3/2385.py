n = int(input())
p, q, r, s, x, y = map(int, input().split())
i, j = map(int, input().split())

a = 0
b = 0
c = 0

for k in range(1, n+1):
    a = ((p*i)+(q*k))%x
    b = ((r*k)+(s*j))%y
    c += a*b

print(c)
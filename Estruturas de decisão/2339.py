c, p, f = input().split()
c = int(c)
p = int(p)
f = int(f)

if p // f >= c:
    print("S")

else:
    print("N")
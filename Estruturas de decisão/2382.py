l, a, p, r = input().split()
l = int(l)
a = int(a)
p = int(p)
r = int(r)

dB = (l**2 + p**2)**0.5
rC = ((dB**2 + a**2)**0.5) / 2

if rC <= r:
    print("S")

else:
    print("N")
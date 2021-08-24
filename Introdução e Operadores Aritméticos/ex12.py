a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

ax = x // a
by = y // b
cz = z // c
tC = (ax*by*cz)

print("{}".format(tC))
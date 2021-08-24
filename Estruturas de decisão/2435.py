a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

h, l, g = input().split()
h = int(h)
l = int(l)
g = int(g)

c1 = (b/1000) / c
c2 = (l/1000) / g

if c1 < c2:
    print("{}".format(a))

else:
    print("{}".format(h))
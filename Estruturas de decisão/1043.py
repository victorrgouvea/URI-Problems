a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a+b > c and a+c > b and b+c > a:
    p = a + b + c
    print("Perimetro = {:.1f}".format(p))

else:
    a = ((a+b)*c) / 2
    print("Area = {:.1f}".format(a))
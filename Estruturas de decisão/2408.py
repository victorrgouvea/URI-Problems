a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if (a > b and a < c) or (a < b and a > c):
    print("{}".format(a))

elif (b > a and b < c) or (b < a and b > c):
    print("{}".format(b))

else:
    print("{}".format(c))

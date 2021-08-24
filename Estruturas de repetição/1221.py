from math import sqrt
n = int(input())
m = 0

while n != 0:
    x = int(input())
    y = int(sqrt(x))
    for c in range(2,(y+1)):
        if (x % c == 0):
            m += 1
            break

    if m == 0:
        print("Prime")
    else:
        print("Not Prime")

    m = 0
    n -= 1
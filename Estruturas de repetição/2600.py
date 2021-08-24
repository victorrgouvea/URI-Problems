n = int(input())

while n != 0:
    x = int(input())
    a, b, c, d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    y = int(input())

    if x+y == 7 and a+c == 7 and b+d == 7 and a != b and a != c and a != d and a != x and a != y and b != a and b != c and b != d and b != x and b != y and c != a and c != b and c != d and c != x and c != y and d != a and d != b and d != c and d != x and d != y and x != a and x != b and x != c and x != d and x != y and y != a and y != b and y != c and y != d and y != x and 1<=a<=6 and 1<=b<=6 and 1<=c<=6 and 1<=d<=6 and 1<=x<=6 and 1<=y<=6:
        print("SIM")

    else:
        print("NAO")

    n -= 1
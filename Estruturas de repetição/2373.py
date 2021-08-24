n = int(input())
q = 0

while n != 0:
    l, c = input().split()
    l = int(l)
    c = int(c)

    if l > c:
        q += c

    n -= 1

print("{}".format(q))
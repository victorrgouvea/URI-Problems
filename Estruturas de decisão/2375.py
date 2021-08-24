n = int(input())
a, l, p = input().split()
a = int(a)
l = int(l)
p = int(p)

if n <= l and n <= a and n <= p:
    print("S")

else:
    print("N")
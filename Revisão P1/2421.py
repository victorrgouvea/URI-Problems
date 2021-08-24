x, y = input().split()
l1, h1 = input().split()
l2, h2 = input().split()
x = int(x)
y = int(y)
l1 = int(l1)
l2 = int(l2)
h1 = int(h1)
h2 = int(h2)

if l2+h1 <= x and h2 <= y and l1 <= y:  #folha de papel na vertical:
    print("S")
elif l1+h2 <= x and h1 <= y and l2 <= y:
    print("S")
elif h2+h1 <= x and l2 <= y and l1 <= y:
    print("S")
elif l2+l1 <= x and h2 <= y and h1 <= y:
    print("S")
elif l2+h1 <= y and h2 <= x and l1 <= x: #folha na horizontal:
    print("S")
elif l1+h2 <= y and h1 <= x and l2 <= x:
    print("S")
elif h2+h1 <= y and l2 <= x and l1 <= x:
    print("S")
elif l2+l1 <= y and h2 <= x and h1 <= x:
    print("S")
else:
    print("N")

'''
if l2+h1 > x and (h2 or l1) > y:
    print("N")
elif l1+h2 > x and (h1 or l2) > y:
    print("N")
elif h1+h2 > x and (l2 or l1) > y:
    print("N")
elif l1+l2 > x and (l2 or l1) > y:
    print("N")
elif h1+h2 <= x and (l2 or l1) > y:
    print("N")
elif l1+l2 <= x and (h2 or h1) > y:
    print("N")
elif h1+l2 <= x and (h2 or l1) > y:
    print("N")
elif l1+h2 <= x and (l2 or h1) > y:
    print("N")

elif l2+h1 > x and (h2 or l1) < y:
    print("N")
elif l1+h2 > x and (h1 or l2) < y:
    print("N")
elif h1+h2 > x and (l2 or l1) < y:
    print("N")
elif l1+l2 > x and (l2 or l1) < y:
    print("N")
else:
    print("S")
'''
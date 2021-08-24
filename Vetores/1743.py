x = input().split()
y = input().split()
comp = True

for i in range(0, 5):
    x[i] = int(x[i])
    y[i] = int(y[i])

for i in range(0, 5):
    if x[i] == y[i]:
        print("N")
        comp = False
        break

if comp:
    print("Y")
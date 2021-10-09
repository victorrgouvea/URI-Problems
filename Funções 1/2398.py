n, k = map(int, input().split())

mat = [0] * n
for i in range(n):
    mat[i] = [0] * n

for _ in range(k):
    x, y, d = map(int, input().split())

    for i in range(n):
        for j in range(n):
            if (abs(x-i) + abs(y-j)) == d:  # Distancia de Manhattan
                mat[i][j] += 1

xT = 0
yT = 0
t = 0
cnt = 0

for i in range(n):
    for j in range(n):
        if mat[i][j] > t:
            t = mat[i][j]
            xT = i
            yT = j
            cnt = 1
        elif mat[i][j] == t:
            cnt += 1

if cnt > 1:
    print("-1 -1")
else:
    print("{} {}".format(xT, yT))
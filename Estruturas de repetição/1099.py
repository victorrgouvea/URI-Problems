n = int(input())
j = 0

for c in range(1 , n + 1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    soma = 0

    if y > x:
        for j in range((x+1), y):
            if (j % 2) != 0:
                soma += j
    elif x > y:
        for j in range((y+1), x):
            if (j % 2) != 0:
                soma += j
    elif x == y:
        soma = 0

    print("{}".format(soma))
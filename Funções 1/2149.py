def phill(x):
    if x == 1:
        return 0
    elif x <= 4:
        return 1
    if x not in memo:
        if (x % 2) == 0:
            memo[x] = phill(x-1) * phill(x-2)
        else:
            memo[x] = phill(x-1) + phill(x-2)
    return memo[x]


memo = {}

while True:
    try:
        n = int(input())
        print(phill(n))

    except EOFError:
        break
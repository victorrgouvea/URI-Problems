def fib(x):
    if x <= 2:
        return 1
    if x not in memo:
        memo[x] = fib(x-1) + fib(x-2)
    return memo[x]


memo = {}
threebonacci = []
k = 0
while len(threebonacci) < 60:
    k += 1
    f = fib(k)
    if (f % 3) == 0 or ('3' in str(f)):
        threebonacci.append(f)

while True:
    try:
        n = int(input())
        print(threebonacci[n-1])

    except EOFError:
        break
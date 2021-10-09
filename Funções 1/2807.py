def fib(x):
    if x <= 2:
        return 1
    if x not in memo:
        memo[x] = fib(x-1) + fib(x-2)
    return memo[x]


memo = {}
n = int(input())

seq = []
for i in range(1, n+1):
    seq.append(fib(i))
seq.sort(reverse=True)

print(seq[0], end='')
for i in range(1, len(seq)):
    print(" %d" % seq[i], end='')
print()
def mdc(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    print(mdc(x, y))
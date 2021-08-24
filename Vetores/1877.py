n, k = map(int, input().split())
t = [int(x) for x in input().split()]

nK = 0

for i in range(1, n-1):
    if t[i] > t[i-1] and t[i] > t[i+1]:
        nK += 1

if nK == k:
    print("beautiful")
else:
    print("ugly")
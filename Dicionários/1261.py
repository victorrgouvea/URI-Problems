m, n = map(int, input().split())

dic = {}
total = 0

for i in range(m):
    p, v = input().split()
    v = float(v)
    dic[p] = v

while n > 0:

    linha = input().split()
    for palavra in linha:
        if palavra in dic:
            total += dic[palavra]

    if linha == ["."]:
        print(int(total))
        total = 0
        n -= 1
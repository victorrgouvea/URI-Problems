n = int(input())
linhaAtual = [int(x) for x in input().split()]

while n > 1:
    proxLinha = [0] * (n-1)
    for i in range(0, n-1):
        if linhaAtual[i] == linhaAtual[i+1]:
            proxLinha[i] = 1
        else:
            proxLinha[i] = -1

    linhaAtual = proxLinha

    n -= 1

if linhaAtual == [1]:
    print("preta")
else:
    print("branca")
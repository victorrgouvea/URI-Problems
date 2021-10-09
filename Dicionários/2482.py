dic = {}

n = int(input())
for i in range(n):
    l = input()
    f = input()
    dic[l] = f

m = int(input())
for i in range(m):
    nome = input()
    lingua = input()
    print(nome)
    print(dic[lingua])
    print("")
n = int(input())
x= 0

for i in range(1,100):
    a = int(input())
    if a > x:
        maior = a
        posicao = i + 1
        x = a

print(maior)
print(posicao)

'''
i = 1
x = 0

while i <= 100:
    n = int(input())
    if n > x:
        maior = n
        posicao = i
        x = n
        i += 1

print("{}".format(maior))
print("{}".format(posicao))
'''
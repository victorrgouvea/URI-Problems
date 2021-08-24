letra = input()
texto = input().split()
count = 0

for i in range(0, len(texto)):
    if letra in texto[i]:
        count += 1

porc = float((count*100) / len(texto))
print('{:.1f}'.format(porc))
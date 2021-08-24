a = int(input())          #entradas das idades da dupla
b = int(input())

if a < 6 or b < 6:        #aplicando a regra de que menores de 6 anos não podem entrar
    print("NO")

elif a >= 18 or b >= 18:  #aplicando a regra de que um dos membros da dupla tem que ter 18 anos ou mais de idade para entrar
    print("YES")

elif a >= 14 and b >= 14: #aplicando a regra de que ambos da dupla tenham pelo menos 14 anos de idade para entrar
    print("YES")

else:                     #negando a entrada de qualquer valores fora das regras acima
    print("NO")
n, m = input().split()    #entrada das variáveis com os números escolhidos
n = int(n)
m = int(m)
p1 = 0                    #variáveis que representam os números primos a serem encontrados
p2 = 0
                          #faremos dois while semelhantes para achar os primos
while n > 1:              #o processo de cada while consiste em testar o número da entrada e seus antecessores até que um primo seja encontrado
    for d in range(2, n): #nessa parte, o número será dividido a partir do número 2 até o número antecessor de n
        if n % d == 0:    #caso alguma dessas divisões dê resto=0, quer dizer que o número testado não é primo e o programa vai parar o funcionamento do for, definir p1 para 0 e começar o processo com o próximo antecessor
            p1 = 0
            break
        else:
            p1 = n        #caso nenhuma divisão dê resto=0, o número testado é primo. Sendo assim, p1 vai ser igual a n e maior que 0, fazendo o while inteiro parar e o número primo encontrado fica armazenado em p1
    if p1 > 0:
        break
    n -= 1


while m > 1:              #processo igual ao descrito acima, trocando apenas o nome das variáveis
    for e in range(2, m):
        if m % e == 0:
            p2 = 0
            break
        else:
            p2 = m
    if p2 > 0:
        break

    m -= 1

print("{}".format(p1*p2))   #impressão do resultado da multiplicação dos primos obtidos, que é a resposta do problema
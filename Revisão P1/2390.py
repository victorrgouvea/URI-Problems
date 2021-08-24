n = int(input()) #input com o número de ativações
tt = 10 #tempo total já começa com 10, pois isso representa a última ativação do sensor sensor
d = 0 #variável que representa a soma dos intervalos de tempo cada vez que o sensor é ativado
p = int(input()) #primeiro tempo que o sensor foi ativado
n -= 1 #subtraindo um valor de n pois ja informamos o primeiro tempo de ativação em p

while n > 0:        #estrutura de repetição para receber e comparar os outros tempos de ativação
    t = int(input()) #input para receber os próximos tempos de ativação
    d += abs(p-t)   #caso o intervalo entre uma atiavação e a próxima seja menor ou igual a dez, vamos adicionar esse intervalo a variável d
    if abs(p-t) > 10: #caso esse intervalo seja maior que 10, o intervalo entre as ativações não deve contar. então vamos subtrair esse intervalo de d e acrescentar 10 segundos no lugar
        d -= abs(p-t)
        d += 10
    p = t            #aqui definimos o valor de t para p, para o valor atual ser comparado com o próximo valor que for adicionado
    n -= 1           #aqui subtraimos um valor de n para o while funcionar corretamente

print("{}".format(tt+d)) #aqui imprimimos o valor do tempo total com a soma dos intervalos de tempo entre as ativações
n, s = input().split()
n = int(n)
s = int(s)
t = 0                   #t será sempre o menor valor que ocorreu no saldo
x = int(input())        #x é o primeiro valor a ser adicionado ou creditado do saldo s
x = x+s                 #aqui tornamos x o saldo total após a primeira operação
if x < s:               #aqui condicionamos qual o saldo menor, se é o saldo original ou o saldo após a operação
   t = x
else:
    t = s
n -= 1

while n > 0:            #aqui vai ser adicionado o valor m em x e compara-lo ao menor valor armazenado em t
    m = int(input())
    x += m
    if x < t:
        t = x           #se o valor for menor, t assume o valor dele
    n -= 1

print("{}".format(t))
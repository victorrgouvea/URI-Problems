n, c = input().split()
n = int(n)
c = int(c)
t = 0 #total de pessoas no elevador
m = 0 #total de ocorrencias de excesso de capacidade

while n > 0:
    s, e = input().split()
    s = int(s)
    e = int(e)
    t += e #adiciona o número de pessoas que entraram no elevador no total
    t -= s #subtrai o número de pessoas que saíram do elevadro no total
    n -= 1
    if t > c: #se a capacidade máxima foi ultrapassada nesse caso, então adiciona +1 a variável m para registrar essa ocorrência
        m += 1

if m > 0:     #se m for maior que 0, significa que foi registrada alguma ocorrencia que a capacidade máxima do elevador foi ultrapassada, logo imprime S
    print("S")
else:
    print("N")
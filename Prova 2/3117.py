alunos, min = map(int, input().split())     #Entradas do número de alunos e da quantidade mínima de pessoas
horarios = list(map(int, input().split()))  #Lista dos horários de chegada de cada aluno
Natrasados = 0   #Variável que representa quantos alunos não estão atrasados

for i in horarios:       #Aqui verificamos se cada aluno está ou não atrasado, e caso não esteja, adicionamos 1 a variável "Natrasados"
    if i <= 0:
        Natrasados += 1

if Natrasados < min:     #Caso o número de alunos que chegaram no horário seja menor que o mínimo imprimi-se "NO"
    print("NO")          #Caso contrário, imprimi-se "YES"
else:
    print("YES")
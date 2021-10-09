n = int(input())  #entrada da quantidade de números de registro

listPresenca = []  #lista que contém os números de registro da lista de presença

#Aqui adiociono os números de registro dos alunos na lista de presença
for i in range(n):
    aluno = int(input())
    listPresenca.append(aluno)

listPresenca = set(listPresenca)  #uso o comando set para eliminar os elementos repetidos, restando apenas uma ocorrência de cada número de registro

print(len(listPresenca))  #como os elementos repetidos foram excluidos da lista, o total de alunos que receberam presença vai ser igual ao número de elementos que a lista de presença possui
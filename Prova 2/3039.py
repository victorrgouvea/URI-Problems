n = int(input())   #Entrada para o número de crianças
carrinhos = 0  #Variáveis com os números de carrinhos e bonecas que devem ser feitos
bonecas = 0

while n > 0:
    c, s = input().split()  #Entrada do nome e sexo da criança
    if s == 'F':        #Aqui condiciono qual presente deve ser feito se a criança é menino ou menina e adiciono 1 ao contador do determinado presente
        bonecas += 1
    else:
        carrinhos += 1

    n -= 1

print("{} carrinhos".format(carrinhos)) #Impressão dos números de carrinhos e bonecas a serem produzidos
print("{} bonecas".format(bonecas))
n, g = map(int, input().split())  # Entrada do número de runas e da quantidade de amizade necessária

dic = {}  # Crio um dicionário para armazenar as runas e seus valores

# Aqui adiciono cada runa com seu valor ao dicionário
for i in range(n):
    r, v = input().split()
    v = int(v)

    dic[r] = v

x = int(input())  # Entrada do número de runas que serão usadas
runas = input().split()  # Entrada das runas que serão usadas, já em forma de lista
amizade = 0  # Variável que armazena o valor de amizade total

# Somo o valor de cada runa usada ao total de amizade
for runa in runas:
    amizade += dic[runa]

print(amizade)  # Imprimo o valor total de amizade

# Faço a impressão baseado em se o valor de amizade das runas foi suficiente ou não
if amizade >= g:
    print("You shall pass!")
else:
    print("My precioooous")
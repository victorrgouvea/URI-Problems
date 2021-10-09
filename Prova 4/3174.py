n = int(input())  # Entrada do número de elfos

# Crio um dicionário para armazenar o total de horas de trabalho de cada grupo
dic = {"bonecos": 0, "arquitetos": 0, "musicos": 0, "desenhistas": 0}

for i in range(n):
    e, g, h = input().split()  # Entrada do nome, grupo e horas que o elfo vai trabalhar
    h = int(h)

    # Adiciono as horas de trabalho do elfo ao total do grupo que ele irá trabalhar
    dic[g] += h

# Aqui pego as horas totais de trabalho de cada grupo e divido pelo tempo necessário para produzir um presente
# Esse resultado será o número de presentes que serão produzidos em um dia de trabalho
# Somo esse valor calculado de cada grupo na variável "total"
total = 0
total += dic["bonecos"] // 8
total += dic["arquitetos"] // 4
total += dic["musicos"] // 6
total += dic["desenhistas"] // 12

print(total)  # Impressão do total de presentes produzidos em um dia
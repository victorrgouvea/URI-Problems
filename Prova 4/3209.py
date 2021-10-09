n = int(input())  # Entrada do número de casos de teste

for _ in range(n):
    v = [int(x) for x in input().split()]  # Lista com o número de réguas e de tomadas
    total = 0  # Variável que armazena o total de aparelhos que podem ser alimentados

    # Aqui somo os números de tomadas de cada régua ao total
    for i in range(1, len(v)):
        total += v[i]

    # Aqui retiro uma tomada do total para cada régua, menos uma, que seria a última a ser utilizada
    # Faço isso pois, para usar outra régua, tenho que usar uma tomada da régua que estou usando
    # Não retiro uma tomada da última régua pois não terei que usar uma tomada dessa régua para conectar outra régua
    total -= (v[0] - 1)

    print(total)  # Imprimo o total de aparelhos que podem ser alimentados
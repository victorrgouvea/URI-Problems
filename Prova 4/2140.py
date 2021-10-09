notas = [100, 50, 20, 10, 5, 2]  # Crio uma lista com as notas disponíveis
while True:
    n, m = map(int, input().split())  # Entrada da compra e do valor pago
    if n == m == 0:
        break

    troco = m - n  # Descubro quanto é o valor do troco
    quant = 0  # Variável que armazena o número de notas necessárias para dar o troco

    # Aqui verifico quantas notas são necessárias para dar o troco a partir das notas disponíveis
    for nota in notas:

        # Caso eu consiga dividir o valor atual do troco pelo valor da nota que estou analisando,
        # eu desconto esse valor do troco e adiciono o número de notas utilizadas em "quant"
        if troco // nota > 0:
            x = troco // nota
            troco -= nota * x
            quant += x

        # Quando o valor do troco chegar a 0, encerro o loop pois já encontrei as notas que preciso
        if troco == 0:
            break

    # Caso o número de notas para para devolver o troco seja igual a 2, é possível devolver o troco exato e imprimo "possible"
    # Caso contrário, não é possível devolver o troco exato e imprimo "impossible"
    if quant == 2:
        print("possible")
    else:
        print("impossible")
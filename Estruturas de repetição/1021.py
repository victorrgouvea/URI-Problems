valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    qntdNota = int(valor / nota)
    print("{} nota(s) de R$ {:.2f}".format(qntdNota, nota))
    valor -= qntdNota*nota

print("MOEDAS:")
for moeda in moedas:
    qntdMoeda = int(round(valor,2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qntdMoeda, moeda))
    valor -= qntdMoeda*moeda
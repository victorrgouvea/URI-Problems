b = int(input())       #entradas da quantidade de bolinhas e do número de galhos, respectivamente
g = int(input())

bN = g // 2           #aqui calculamos quantas bolinhas são necessárias para completar a árvore
bF = bN - b           #aqui calculamos quantas bolinhas estão faltando

if bF <= 0:                                  #aqui condicionamos a impressão do resultado dependendo de quantas bolinhas faltam
    print("Amelia tem todas bolinhas!")
else:
    print("Faltam {} bolinha(s)".format(bF))
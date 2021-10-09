# Função para calcular o MDC
def mdc(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


# Função para calcular o MMC a partir do MDC
def mmc(a, b):
    cima = a*b
    baixo = mdc(a, b)
    return cima/baixo


while True:
    try:
        m = int(input())  # Entrada do tempo desde o último alinhamento
        x, y, z = map(int, input().split())  # Entradas dos tempos para cada lua completar uma volta

        # O mmc dos tempos de cada lua completar uma volta é igual ao alinhamento lunar
        # Calculo primeiro o mmc entre x e y, e pego esse resultado e calculo o mmc com z para achar o mmc entre os 3
        alinhamento = mmc((mmc(x, y)), z)

        anos = alinhamento - m  # Calculo quantos anos faltam para o alinhamento acontecer

        print(int(anos))  # Imprimo essa quantidade de anos

    except EOFError:
        break
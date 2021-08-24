n = int(input())
casa = 0
trab = 0
ficouc = 0
ficout = 0

while n > 0:
    ida, volta = input().split()
    if ida == 'chuva':
        if ficouc > 0:
            ficouc -= 1
            ficout += 1
        else:
            casa += 1
            ficout += 1

    if volta == 'chuva':
        if ficout > 0:
            ficout -= 1
            ficouc += 1
        else:
            trab += 1
            ficouc += 1

    n -= 1

print('{} {}'.format(casa, trab))
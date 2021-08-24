n = int(input())
cod = ['GQaku', 'ISblv', 'EOYcmw', 'FPZdnx', 'JTeoy', 'DNXfpz', 'AKUgq', 'CMWhr', 'BLVis', 'HRjt']

while n > 0:
    frase = input().replace(' ', '')
    fcod = []
    for i in range(0, 12):
        for j in range(0, 10):
            if frase[i] in cod[j]:
                fcod.append(str(j))
                break
    fcod = ''.join(fcod)
    print(fcod)

    n -= 1
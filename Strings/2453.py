msg = input().split()
msgdecod = ''

for palavra in msg:
        for letra in range(1, len(palavra), 2):
            msgdecod += palavra[letra]
        msgdecod += ' '

print(msgdecod[:-1])
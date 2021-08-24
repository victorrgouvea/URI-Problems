n = int(input())

while n > 0:
    msgcod = input()
    msgcod = list(msgcod)
    msg = []
    for i in range(0, len(msgcod)):
        if msgcod[i].islower():
            msg.append(msgcod[i])
    msg = ''.join(msg)
    msg = msg[::-1]
    print(msg)

    n -= 1
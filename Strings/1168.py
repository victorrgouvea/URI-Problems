n = int(input())

while n > 0:
    led = 0
    v = input()
    for i in range(0, len(v)):
        if v[i] == '1':
            led += 2
        if v[i] == '2':
            led += 5
        if v[i] == '3':
            led += 5
        if v[i] == '4':
            led += 4
        if v[i] == '5':
            led += 5
        if v[i] == '6':
            led += 6
        if v[i] == '7':
            led += 3
        if v[i] == '8':
            led += 7
        if v[i] == '9':
            led += 6
        if v[i] == '0':
            led += 6

    print("{} leds".format(led))

    n -= 1
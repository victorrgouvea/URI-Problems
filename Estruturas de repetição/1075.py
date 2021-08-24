n = int(input())
i = 1

while i <= 10000:
    x = i % n
    if x == 2:
        print("{}".format(i))
    i += 1
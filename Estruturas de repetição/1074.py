n = int(input())

while n != 0:
    x = int(input())
    xp = x % 2
    if xp == 0 and x > 0:
        print("EVEN POSITIVE")
    elif xp == 0 and x < 0:
        print("EVEN NEGATIVE")
    elif xp != 0 and x > 0:
        print("ODD POSITIVE")
    elif xp != 0 and x < 0:
        print("ODD NEGATIVE")
    elif x == 0:
        print("NULL")
    n -= 1
while True:
    n = int(input())
    if n == 0:
        break

    dic = {}
    v = input().split()

    for numero in v:
        if numero in dic:
            dic[numero] += 1
        else:
            dic[numero] = 1

    for key in dic:
        if (dic[key] % 2) != 0:
            print(key)
            break
while True:
    try:
        dic = {"EPR" : 0, "EHD" : 0, "INTRUSOS" : 0}

        n = int(input())
        for i in range(n):
            m, s = input().split()
            if s in dic:
                dic[s] += 1
            else:
                dic["INTRUSOS"] += 1

        print("EPR: {}".format(dic["EPR"]))
        print("EHD: {}".format(dic["EHD"]))
        print("INTRUSOS: {}".format(dic["INTRUSOS"]))

    except EOFError:
        break
dic = {"X" : 0, "H" : 0, "E" : 0, "A" : 0, "M" : 0}

n = int(input())

for i in range(n):
    nome, raca = input().split()
    dic[raca] += 1

print("{} Hobbit(s)".format(dic["X"]))
print("{} Humano(s)".format(dic["H"]))
print("{} Elfo(s)".format(dic["E"]))
print("{} Anao(s)".format(dic["A"]))
print("{} Mago(s)".format(dic["M"]))
x = str(input())
y = str(input())
z = str(input())

if x == "vertebrado":
    if y == "ave":
        if z == "carnivoro":
            print("aguia")

        elif z == "onivoro":
            print("pomba")

    elif y == "mamifero":
        if z == "onivoro":
            print("homem")

        elif z == "herbivoro":
            print("vaca")

elif x == "invertebrado":
    if y == "inseto":
        if z == "hematofago":
            print("pulga")

        elif z == "herbivoro":
            print("lagarta")

    elif y == "anelideo":
        if z == "onivoro":
            print("minhoca")

        elif z == "hematofogo":
            print("sanguessuga")
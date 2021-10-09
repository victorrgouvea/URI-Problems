n = int(input())  # Entrada do número de casos

for _ in range(n):
    cartas = input()  # Entrada da string com as cartas que sobraram

    # Aqui verifico se cada uma das cartas da superstição está entre as cartas que sobraram
    # Caso todas estejam, imprimo "Aaah muleke"
    # Caso ao menos uma não esteja, imprimo "Ooo raca viu"
    if 'A' in cartas:
        if 'Q' in cartas:
            if 'K' in cartas:
                if 'J' in cartas:
                    print("Aaah muleke")

                else:
                    print("Ooo raca viu")

            else:
                print("Ooo raca viu")

        else:
            print("Ooo raca viu")

    else:
        print("Ooo raca viu")
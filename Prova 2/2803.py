norte = ['roraima', 'acre', 'amapa', 'amazonas', 'para', 'rondonia', 'tocantins']  #Vetor com todos os estados da região norte
estado = input()          #Entrada do nome do estado em questão

if estado in norte:       #Daqui para baixo, verfico se o estado da entrada está ou não na lista de estados do norte, e então imprimo a mensagem baseada nesse verificação
    print("Regiao Norte")
else:
    print("Outra regiao")
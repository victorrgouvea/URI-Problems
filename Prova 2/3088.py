while True:
    try:
        frase = input()      #Entrada da frase incorreta
        fraseCorreta = ''    #String que vai armazenar a frase corrigida

        for i in range(0, len(frase)-1):                                      #Neste for, iremos percorrer toda a entrada "frase", menos o seu último termo
            if frase[i] == ' ' and (frase[i+1] == ',' or frase[i+1] == '.'):  #Verificaremos se o elemento da string é um espaço e se o seu próximo elemento é um ponto ou uma vírgula
                fraseCorreta += ''                                            #Caso a condição acima for verdadeira, nada será adicionado a string "fraseCoreta", e assim será feita a correção pedida na questão
            else:                                                             #Caso contrário, o próprio elemento será adicionado a string
                fraseCorreta += frase[i]

        fraseCorreta += frase[len(frase)-1]    #Aqui adicionamos o último elemento da string "frase", que não foi verificado no for, na string "fraseCorreta
        print(fraseCorreta)    #Impressão da frase com as correções aplicadas

    except EOFError:
        break
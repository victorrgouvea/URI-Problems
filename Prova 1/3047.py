m = int(input())         #entrada com os valores das idades da mãe e dos dois filhos
a = int(input())
b = int(input())

c = m - (a+b)            #cálculo da idade do terceiro filho

if a > b and a > c:      #aqui identificamos qual filho é o mais velho e imprimimos sua idade
    print("{}".format(a))

elif b > a and b > c:
    print("{}".format(b))

else:
    print("{}".format(c))
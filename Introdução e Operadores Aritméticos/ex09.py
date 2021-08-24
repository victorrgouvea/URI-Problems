#anos - meses - dias

i = int(input())

a = i // 365
m = (i % 365) // 30
d = ((i % 365) % 30) % 30

print("{} ano(s)" .format(a))
print("{} mes(es)" .format(m))
print("{} dia(s)" .format(d))

'''
horas - minutos - segundos
n = int(input())

h = n // 3600
m = (n % 3600) // 60
s = ((n % 3600) % 60) % 60

print("{}:{}:{}" .format(h, m, s))
'''
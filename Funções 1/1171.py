def add_list(x):
    if x not in num_cresc:
        num_cresc.append(x)
    num_total.append(x)


num_cresc = []
num_total = []

n = int(input())
for _ in range(n):
    a = int(input())
    add_list(a)

num_cresc.sort()

for num in num_cresc:
    print("{} aparece {} vez(es)".format(num, num_total.count(num)))
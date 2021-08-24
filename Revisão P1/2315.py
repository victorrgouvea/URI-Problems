t = [31,28,31,30,31,30,31,31,30,31,30,31]
d1, m1 = input().split()
d2 ,m2 = input().split()
d1 = int(d1)
m1 = int(m1)
d2 = int(d2)
m2 = int(m2)
i = 0
j = 0

for x in range(m1-1, len(t)):
    i += t[x]
for x in range(m2-1, len(t)):
    j += t[x]

i -= d1
j -= d2

print("{}".format(abs(j-i)))
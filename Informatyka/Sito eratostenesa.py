#zad.1
#Sito Erotostenesa - algortm podstawowy
n = int(input())
T = [True] * (n+1)
T[0] = False
T[1] = False
p = 2
while p*p <= n:
    if T[p]:
        for i in range(p*p,n+1,p):
            T[i] = False
    p += 1
for i in range(2,n+1):
    if T[i] == True:
        print(i, end=" ")

#Zad.1
n = int(input())
czynnik = 2
while n >1:
    while n%czynnik==0:
        print(czynnik)
        n = n//czynnik
    czynnik+=1

#Zad.2
n = int(input())
czynnik = 2
suma = 0
while n >1:
    while n%czynnik==0:
        suma += czynnik
        n = n//czynnik
    czynnik+=1
print(suma)

#Zad.3
def czy_pierwsza(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n = int(input())
czynnik = 2
suma = 0
while n >1:
    while n%czynnik==0:
        suma += czynnik
        n = n//czynnik
    czynnik+=1
if czy_pierwsza(suma):
    print("Tak")
else:
    print("Nie")

#Zad.4
n = int(input())
licz_pierwsze = []
czynnik = 2
while n >1:
    while n%czynnik==0:
        if czynnik not in licz_pierwsze:
            licz_pierwsze.append(czynnik)
        n = n//czynnik
    czynnik+=1
print(licz_pierwsze)

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

#Zad.5
from math import sqrt
def czy_zlozona(n):
    if n<2:
        return False
    p=int(sqrt(n))
    for i in range(2, p+1):
        if n%i==0:
            return True
    return False

def suma_cyfr(n):
    suma = 0
    while n>0:
        suma += n%10
        n//=10
    return suma
def suma_cyfr_czynnikow(n):
    czynnik = 24
    suma = 0
    while n > 1:
        while n % czynnik == 0:
            suma += suma_cyfr(czynnik)
            n //= czynnik
        czynnik += 1
    return suma

n = int(input())

if czy_zlozona(n) and suma_cyfr(n) == suma_cyfr_czynnikow(n):
    print("tak")
else:
    print("nie")

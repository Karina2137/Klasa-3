from math import sqrt
def czy_pierwsza(n):
    if n<2:
        return False
    p=int(sqrt(n))
    for i in range(2, p+1):
        if n%i==0:
            return False
    return True
    
#Zad.1
plik = open("liczby1.txt","r") #otwieranie pliku
liczby = list(map(int,plik.read().split())) #tworzenie listy z zawartości pliku
ile = 0
for liczba in liczby:
    if czy_pierwsza(liczba):
        ile += 1
print(ile)
plik.close() #zamknięcie pliku

#Zad.2
plik = open("liczby2.txt","r")
liczby = list(map(int,plik.read().split()))
for liczba  in liczby:
    if liczba % 2 == 0:
        print(liczba, end="\n")
plik.close()

#Zad.3
def liczba_dzielnikow_wlasciwych(n):
    ile = 0
    for i in range(1,n):
        if n % i == 0:
            ile += 1
    return ile
plik = open("liczby2.txt","r")
liczby = list(map(int,plik.read().split()))
plik.close()
suma = 0
for liczba in liczby:
    suma+=liczba_dzielnikow_wlasciwych(liczba)
print(suma)

#Zad.5
def suma_czynnikow_pierwszych(n):
    czynnik = 2
    suma = 0
    while n>1:
        while n % czynnik == 0:
            suma += czynnik
            n //= czynnik
        czynnik += 1
    return suma
plik = open("liczby2.txt","r")
liczby = list(map(int,plik.read().split()))
plik.close()
suma_czynnikow = []
for liczba in liczby:
    suma_czynnikow.append(suma_czynnikow_pierwszych(liczba))
minimum = min(suma_czynnikow)
for i in range(len(liczby)):
    if suma_czynnikow[i] == minimum:
        print(liczby[i])

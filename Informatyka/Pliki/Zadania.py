from math import sqrt
def czy_pierwsza(n):
    if n<2:
        return False
    p=int(sqrt(n))
    for i in range(2, p+1):
        if n%i==0:
            return False
    return True

plik = open("liczby1.txt","r") #otwieranie pliku
liczby = list(map(int,plik.read().split())) #tworzenie listy z zawartości pliku
#Zad.1
ile = 0
for liczba in liczby:
    if czy_pierwsza(liczba):
        ile += 1
print(ile)
plik.close() #zamknięcie pliku

#zad.1
def wyswietl_liczby_po_spacji(tablica):
    print(' '.join(map(str,tablica)))
plik = open('liczby.txt', 'r')
ciag = list(map(int,plik.read().split()))
plik.close()
print(ciag)
n = len(ciag)
for dl in range(1,n+1):
    for indeks_pocz in range(n-dl+1):
        wyswietl_liczby_po_spacji(ciag[indeks_pocz:indeks_pocz+dl])

#wersja bez slajsingu    
def wyswietl_liczby_po_spacji(tablica):
    print(' '.join(map(str,tablica)))
plik = open('liczby.txt', 'r')
ciag = list(map(int,plik.read().split()))
plik.close()
print(ciag)
n = len(ciag)
for dl in range(1,n+1):
    for indeks_pocz in range(n-dl+1):
        indeks_kon = indeks_pocz+dl-1
        for i in range(indeks_pocz, indeks_kon+1):
            print(ciag[i], end=" ")
        print()

#zad.2
plik = open('liczby.txt', 'r')
ciag = list(map(int,plik.read().split()))
plik.close()
print(ciag)
n = len(ciag)
for index_pocz in range(n):
    for dl in range(1, n+1-index_pocz):
        print(*ciag[index_pocz:index_pocz+dl])
    print()

#zad.6
ciag = list(map(int, input("Podaj ciąg liczb: ").split(' ')))
def czy_rosnąca(tab):
    n = len(tab)
    for i in range(1, n):
        if tab[i] <= tab[i-1]:
            return ("nie")
    return ("tak")
print(czy_rosnąca(ciag))

#zad.7
def czy_malejąca(tab):
    n = len(tab)
    for i in range(1, n):
        if tab[i] >= tab[i-1]:
            return ("nie")
    return ("tak")
print(czy_malejąca(ciag))

#zad.8
def czy_nierosnący(tab):
    n = len(tab)
    for i in range(1, n):
        if tab[i] > tab[i-1]:
            return ("nie")
    return ("tak")
print(czy_nierosnący(ciag))

#zad.9
def czy_niemalejący(tab):
    n = len(tab)
    for i in range(1, n):
        if tab[i] < tab[i-1]:
            return ("nie")
    return ("tak")
print(czy_niemalejący(ciag))

#zad.10
def czy_równy(tab):
    n = len(tab)
    for i in range(1, n):
        if tab[0] != tab[i]:
            return ("nie")
    return ("tak")
print(czy_równy(ciag))

#zad.11
plik = open('liczby.txt', 'r')
ciag = list(map(int,plik.read().split()))
plik.close()

aktualna_dludosc = 1
maks_dlugosc = 0
n = len(ciag)
for i in range(1,n):
    if ciag[i]>=ciag[i-1]:
        aktualna_dludosc+=1
        if aktualna_dludosc>maks_dlugosc:
            maks_dlugosc=aktualna_dludosc
    else:
        aktualna_dludosc=1
print(maks_dlugosc)

#zad.12
plik = open('liczby.txt', 'r')
ciag = list(map(int,plik.read().split()))
plik.close()

aktualna_dludosc = 1
maks_dlugosc = 0
n = len(ciag)
index_pocz_akt = 0
index_pocz_maks = 0
for i in range(1,n):
    if ciag[i]>=ciag[i-1]:
        aktualna_dludosc+=1
        if aktualna_dludosc>maks_dlugosc:
            maks_dlugosc=aktualna_dludosc
            index_pocz_maks = index_pocz_akt
    else:
        aktualna_dludosc=1
        index_pocz_akt = i
print(maks_dlugosc, ciag[index_pocz_maks:index_pocz_maks + maks_dlugosc])

#Zadanie maturalne
#zad3.1
plik = open("pi.txt", "r")
LiczbyPi = list(map(int, plik.read().split()))
plik.close()
for i in range(90):
    liczba = LiczbyPi[i] * 10 + LiczbyPi[i + 1]
    
    if liczba > 90:
        print(liczba)

#zad3.2
T = [0] * 100

for i in range(len(LiczbyPi) - 1):
    liczba = LiczbyPi[i] * 10 + LiczbyPi[i + 1]
    T[liczba] += 1
maks = max(T)
mini = min(T)
if T.index(mini) > 10:
    print(f"Najmniej wystąpień ma: {T.index(mini)} {mini}")
else:
    print(f"Najmniej wystąpień ma: 0{T.index(mini)} {mini}")
print(f"Najwięcej wystąpień ma: {T.index(maks)} {maks}")


#zad3.4

def  czy_rosnaco_malejaca(ciag):
    czy_maleje = False
    n = len(ciag)
    if n < 4 or ciag[2]<=ciag[1]:
        return False
    for i in range(1,n-1):
        if ciag[i+1]>ciag[i]:
            if czy_maleje:
                return False
        elif ciag[i+1]<ciag[i]:
            czy_maleje=True
        else:
            if czy_maleje==False:
                czy_maleje=True
            else:
                return True
    return True
            

n = len(LiczbyPi)
for i in range (n):
    j=i+4
    while czy_rosnaco_malejaca(LiczbyPi[i:j]):
        if j>=
        
        
# trydny sposób(niedokończony)
# czy_rosnie = True
# fragment = [LiczbyPi[0]]
# n = len(LiczbyPi)
# for i in range (1, n):
#     if czy_rosnie and LiczbyPi[-1] > fragment[-1]:
#         fragment.append(LiczbyPi[i])
#     else:
#         czy_rosnie=False
#         fragment.append(LiczbyPi[i])
#     if  !czy_rosnie and LiczbyPi[i] < fragment[-1]:
#         fragment.append(LiczbyPi[i])
#     else:

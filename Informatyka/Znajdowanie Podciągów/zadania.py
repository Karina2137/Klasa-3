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

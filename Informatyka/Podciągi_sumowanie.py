plik = open('ciag.txt', 'r')
ciag = list(map(int, plik.read().split))
plik.close()

#zad.4
maksSuma = 0
aktSuma = 0
n = len(ciag)
for i in range(n):
    aktSuma += ciag[i]
    if aktSuma < 0:
        aktSuma = 0
    elif aktSuma > maksSuma:
        maksSuma = aktSuma

print(maksSuma)

#zad.5
maksSuma = 0
aktSuma = 0
pocz_akt = 0
pocz_maks = 0
kon_maks = 0
n = len(ciag)
for i in range(n):
    aktSuma += ciag[i]
    if aktSuma < 0:
        aktSuma = 0
        pocz_akt =i+1
    elif aktSuma > maksSuma:
        maksSuma = aktSuma
        pocz_maks = pocz_akt
        kon_maks = i
print(maksSuma, ciag[pocz_maks:kon_maks+1])

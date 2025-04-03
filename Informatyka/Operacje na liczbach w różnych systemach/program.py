#zad.2
#versja 1
# liczba1 = int(input("Podaj liczbę binarną: "), 2)
# liczba2 = int(input("Podaj liczbę binarną: "), 2)
# suma = liczba1+liczba2
# print(bin(suma)[2:])
#
# #versja 2
# bin1 = input("Podaj liczbę binarną: ")
# bin2 = input("Podaj liczbę binarną: ")
# wynik = ""
# dl_1 = len(bin1)
# dl_2 = len(bin2)
# if dl_1>dl_2:
#     bin2="0"*(dl_1-dl_2)+bin2
#     dl_2=dl_1
# else:
#     bin1 = "0" * (dl_2 - dl_1) + bin1
#     dl_1 = dl_2
# przeniesienie = 0
# for i in range(dl_1-1,-1,-1):
#     cyfra_wyniku=int(bin1[i])+int(bin2[i])+przeniesienie
#     if cyfra_wyniku>1:
#         przeniesienie=1
#         cyfra_wyniku=cyfra_wyniku%2
#     else:
#         przeniesienie=0
#     wynik = str(cyfra_wyniku) + wynik
# if przeniesienie==1:
#     wynik = "1" + wynik
# print(wynik)

import math
#zad.3
def konversja_na_dec(liczba, podstawa):
    for i in range(len(liczba)):
        ost_cyfra = int(liczba%10)
        wynik = ost_cyfra*math.pow(podstawa,i)
    return wynik
#versja 1
p = int(input("Podaj podstawę: "))
liczba1 = int(input("Podaj liczbę: "), p)
liczba2 = int(input("Podaj liczbę: "), p)
suma = liczba1+liczba2
print(konversja_na_dec(str(suma), p))

#versja 2
bin1 = input("Podaj liczbę binarną: ")
bin2 = input("Podaj liczbę binarną: ")
wynik = ""
dl_1 = len(bin1)
dl_2 = len(bin2)
if dl_1>dl_2:
    bin2="0"*(dl_1-dl_2)+bin2
    dl_2=dl_1
else:
    bin1 = "0" * (dl_2 - dl_1) + bin1
    dl_1 = dl_2
przeniesienie = 0
for i in range(dl_1-1,-1,-1):
    cyfra_wyniku=int(bin1[i])+int(bin2[i])+przeniesienie
    if cyfra_wyniku>1:
        przeniesienie=1
        cyfra_wyniku=cyfra_wyniku%2
    else:
        przeniesienie=0
    wynik = str(cyfra_wyniku) + wynik
if przeniesienie==1:
    wynik = "1" + wynik
print(wynik)

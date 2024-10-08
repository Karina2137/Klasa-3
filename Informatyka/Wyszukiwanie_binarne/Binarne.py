def czy_nie_malejaca(T,n):
    for i in range(n-1):
        if T[i] > T[i+1]:
            return False
    return True

#Zad.1
def wyszukiwanie_binarne(T, a, n):
    lewy = 0
    prawy = n-1
    while lewy < prawy:
        srodek = (lewy+prawy)//2
        if T[srodek] < a:
            lewy = srodek+1
        else:
            prawy = srodek
        if T[lewy]==a:
            return T[lewy]
            
L = list(map(int, input().split()))
l = int(input())
if czy_nie_malejaca(L,L(len)):
    print(wyszukiwanie_binarne(L,l,len[L]))
else:
    print("Nie")

#Zad.2
def wyszukiwanie_binarne_rek(T, a, lewy, prawy):
    if lewy < prawy:
        srodek = (lewy+prawy)//2
        if T[srodek] < a:
            return wyszukiwanie_binarne_rek(T, a, srodek+1, prawy)
        else:
            return wyszukiwanie_binarne_rek(T, a, lewy, srodek)
    return T[lewy] == a
T = list(map(int, input().split()))
a = int(input())
if czy_nie_malejaca(T,len(T)):
    print(wyszukiwanie_binarne_rek(T, a, 0, len(T)-1))
else:
    print("Ciąd musi być uporządkowany")

def czy_nie_malejaca(T,n):
    for i in range(n-1):
        if not T[i] > T[i+1]:
            return False
        return True

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
T = [1,2,3,4,5,6,7,8,9,10]
print(wyszukiwanie_binarne(T,4,10))
print()

#Zad.1
L = []
l = int(input())
for i in range(10):
    n = int(input())
    L.append(n)

if czy_nie_malejaca(T,T(len)):
    print(wyszukiwanie_binarne(L,l,len[L]))
else:
    print("Nie")

#Zad.2

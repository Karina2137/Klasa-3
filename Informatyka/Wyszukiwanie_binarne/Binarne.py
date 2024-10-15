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
#Zad.3
plik1 = open("ciagi.txt", "r")
Ciagi1 = plik1.readlines()
plik1.close()

for ciag in Ciagi1:
    C = list(map(int, ciag.split()))
    if wyszukiwanie_binarne_rek(C, 10, 0, len(C) - 1):
            print(C)
#Zad.4
plik2 = open("ciagi2.txt","r")
n = int(plik2.readline().rstrip())
for i in range(n):
    d = int(plik2.readline().rstrip())
    ciag = list(map(int,plik2.readline().split()))
    if wyszukiwanie_binarne(ciag, 10, d):
        print(ciag)
plik2.close()

# zad.5 (pseudokod)
#def czy_nie_malejaca(T,n):
#     for i in range(1,n+1):
#         if T[i] > T[i+1]:
#             return False
#     return True
# funkcja wyszukiwanie_binarne(T, a, n):
#     lewy ← 1
#     prawy ← n
#     dopóki lewy<prawy wykonuj:
#       srodek ← (lewy + prawy) div 2
#       jeżeli T[srodek] < a to:
#           lewy ← srodek +1
#       w przeciwnym wypadku:
#           prawy ← srodek
#     zwróć T[lewy] = a i zakończ
# T = list(map(int, input().split()))
# T.insert(0, 0)
# a = int(input())
# if czy_nie_malejaca(T,len(T)-1):
#     print(wyszukiwanie_binarne_rek(T, a, 0, len(T)-1))
# else:
#     print("Ciąd musi być uporządkowany")
# zad.7
# n = 10
# A=[0, 5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
# rozwiązanie: ↓
#a)python
# i = 1
# while i<=n:
#     if A[i]%2==0:
#         w=A[i]
#         break
#     i=i+1
# print(w)
#b)pseudokod
# i←1
# dopóki i<= wykonuj:
#     jeżeli A[i] mod 2 = 0 to:
#         w← A[i]
#         zwróć w i zakończ
# i←i+1
#c)inny sposób (lepiej punktowany)
n = 10
A=[0, 5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
lewy = 1
prawy = n
while lewy < prawy:
    srodek = (lewy + prawy) // 2
    if A[srodek]%2==1:
        lewy = srodek + 1
    else:
        prawy = srodek
w = A[lewy]

# def scal(T,lewy,srodek,prawy):
#     i=lewy
#     j=srodek+1
#     k=lewy
#     pom = [0] * (prawy-1)
#     while i<=srodek and j<=prawy:
#         if T[i]<T[j]:
#             pom[k] = T[i]
#             i+=1
#         else:
#             pom[k] = T[j]
#             j+=1
#         k+=1
#     while i<=srodek:
#         pom[k]=T[i]
#         i+=1
#         k+=1
#     while j<=srodek:
#         pom[k]=T[j]
#         j+=1
#         k+=1
#     for i in range(lewy,prawy):
#         T[i] = pom[i]
#
# def sortuj(T,lewy,prawy):
#     if lewy<prawy:
#         srodek = (lewy+prawy)//2
#         sortuj(T,lewy,srodek)
#         sortuj(T,srodek+1,prawy)
#         scal(T,lewy,srodek,prawy)
#
# T = list(map(int,input().split(" ")))
# sortuj(T,0,len(T)-1)

#Zad.1
def scal(t1,t2):
    wynik = []
    i=0
    j=0
    n1=len(t1)
    n2=len(t2)
    while i<n1 and j<n2:
        if t1[i] < t2[j]:
            wynik.append(t1[i])
            i+=1
        else:
            wynik.append(t2[j])
            j+=1
    wynik.extend(t1[i:])
    wynik.extend(t2[j:])
    return wynik

def sortowanie_przez_scalanie(t):
    n = len(t)
    if n>1:
        srodek = (n-1)//2
        lewy = sortowanie_przez_scalanie(t[:srodek+1])
        prawy = sortowanie_przez_scalanie(t[srodek+1:])
        return scal(lewy,prawy)
    return t

ciag = input("Podaj ciąg")
liczby = list(map(int, ciag.split()))
print(liczby)
liczby = sortowanie_przez_scalanie(liczby)
print(liczby)

#zad.2
plik = open("ciagi.txt", "r")
k = plik.readline()
k = list(map(int,k.split()))
l = plik.readline()
l = list(map(int, l.split()))
wynik = scal(k,l)
plik = open("wyniki_2.txt","w")
plik.write(" ".join(map(str, wynik)))
# s = ""
# for e in wynik:
#     s += str(e)
# print(s[:-1])

#Zad.3
import random
liczby = [random.randint(1,1000000) for i in range(1000000)]
liczby = sortowanie_przez_scalanie(liczby)
with open("wyniki_3.txt", "w") as plik:
    for e in liczby:
        plik.write(f"{e}\n")

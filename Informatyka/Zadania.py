#Adres strony z zadaniami: tiny.pl/j08n-qy6

#def czy_podielna_przez_2(n):
#    return n % 2 == 0

#Zad.1
# n = int(input("Podaj liczbę: "))
# if czy_podielna_przez_2(n):
#     print("Tak")
# else:
#     print("Nie")

#Zad.2
#a) złożóność - n
m = int(input("Podaj Liczbę: "))
# for i in range(1, m+1):
#     if m % i == 0:
#         print(i)
#b)złożóność - pierwiastek z n
# i = 1
# while i*i<n:
#     if n%i==0:
#         print(i)
#         print(int(n/i))
#     i=i+1
# if i*i==n:
#     print(i)

#Zad.3
# l = int(input("Podaj Liczbę: "))
# suma = 0
# for i in range(1, l+1):
#     if l % i == 0:
#         suma += i
# print(suma)

#Zad.4
# p = int(input("Podaj Liczbę: "))
# ilosc_dzielnikow = 0
# for i in range(1, p+1):
#     if p % i == 0:
#         ilosc_dzielnikow += 1
# print(ilosc_dzielnikow)

#Zad.5
import math

def czy_pierwsza(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0: return False
    return True

# n = int(input("Podaj n: "))
# for i in range(2, n+1):
#     if n % i == 0 and czy_pierwsza(i):
#         print(i)

#Zad.6
# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# if czy_pierwsza(a) and czy_pierwsza(b) and (math.ceil(a-b)==2 or math.ceil(b-a)==2): print(f"Liczby {a} i {b} są bliźniacze")
# else: print(f"Liczby {a} i {b} nie są bliźniacze")

#Zad.7

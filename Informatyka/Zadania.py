#Adres strony z zadaniami: tiny.pl/j08n-qy6

# #zad.1
a = int(input())
if a%2==0:
    print("tak")
else:
    print("nie")
# #zad.2
b = int(input())
for i in range(1,b+1):
    if b%i==0:
        print(i, end=" ")
print()
#b)złożóność - pierwiastek z n
# i = 1
# while i*i<n:
#     if n%i==0:
#         print(i)
#         print(int(n/i))
#     i=i+1
# if i*i==n:
#     print(i)
# #zad.3
c = int(input())
suma = 0
for i in range(1,c+1):
    if c%i==0:
        suma += i
print(suma)
#zad.5
def czy_pierwsza(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

d = int(input())
for i in range(2,d):
    if d%i==0 and czy_pierwsza(i):
        print(i, end=" ")

#zad.6
def czy_pierwsza(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

e = int(input())
f = int(input())
if czy_pierwsza(e) and czy_pierwsza(f):
    if e-f==2 or f-e==2:
        print("tak")
    else:
        print("nie")
else:
    print("nie")

#zad.7
g = int(input())
suma=0
for i in range(1,g):
    if g%i==0:
        suma+=i
if suma == g:
    print("tak")
else:
    print("nie")

#zad.8
h = int(input())
j = int(input())
suma_h = 0
suma_j = 0
for i in range(1,h):
    if h%i==0:
        suma_h += i
for i in range(1,j):
    if j%i==0:
        suma_j += i
if suma_h == j and suma_j == h and j!=h:
    print("tak")
else:
    print("nie")

#zad.9
def czy_pierwsza(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

for i in range(1,1001):
    if czy_pierwsza(i) and czy_pierwsza(i+2):
        print(i,i+2)

#zad.10
def suma_dzielnikow_wlasciwych(n):
    suma = 0
    for i in range(1,n):
        if n%i==0:
            suma+=i
    return suma
for i in range(1,1001):
    if suma_dzielnikow_wlasciwych(i) == i:
        print(i, end=" ")

# zad.1
plik = open("dane_osobowe.txt", "w")
a = input("Podaj imię: ")
plik.write(a + "\n")
b = input("Podaj nazwisko: ")
plik.write(b)
plik.close()

# zad.2
plik2 = open("dane_osobowe.txt", "r")
linia = plik2.readline()
lista = list(map(str, linia.rstrip()))
# print(f"Witaj {lista[2]} {lista[3]}")
plik2.close()

# zad.4
plik = open("ciagi.txt", "r")
suma = 0
for linia in plik:
    ilosc  = 0
    linia = linia.split()
    for i in range(len(linia)):
        ilosc+=1
    if ilosc % 2==0:
        suma+=1
print(suma)

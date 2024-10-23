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

# zad.5
print("a. wyświetli ponumerowane słowa z pliku tekstowego")
plik = open('slowa.txt','r')
slowa = list(map(str,plik.readlines()))
for i in range(len(slowa)):
    print(f"{i+1}.{slowa[i]}")
print("b. wyświetli liczbę słów w pliku")
ilosc = 0
for i in range(len(slowa)):
    ilosc+=1
print(ilosc)
print("c. wyświetli słowa zaczynające się na literę A")
for i in range(len(slowa)):
    if (slowa[i])[0] == "A":
        print(slowa[i])
print("d. wyświetli słowa kończące się na literę A")
for i in range(len(slowa)):
    if (slowa[i])[-1] == "A":
        print(slowa[i])
print("e. wyświetli słowa oraz liczbę liter, z których się składają")
for slowo in slowa:
    print(f"{len(slowo)-1} - slowo")
print("f. *wyświetli najkrótsze oraz najdłuższe słowo w pliku oraz ich długość (jeżeli jest ich kilka wyświetlpierwsze z nich)")
print("g. wyświetli słowa o długości 6")
print("h. wyświetli słowa zawierające literę O oraz dla każdego z tych słów liczbę tych liter O")
print("i. wyświetli ile razy w całym pliku występuje litera A")
plik.close()

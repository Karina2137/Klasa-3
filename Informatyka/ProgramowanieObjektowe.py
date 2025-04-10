from math import sqrt
class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.a =dlugosc
        self.b =szerokosc
    def pole(self):
        return self.a*self.b
    def obwod(self):
        return self.a*2+self.b*2

class ProstokatExtra(Prostokat):
    def __init__(self, a, b):
        super().__init__(a,b)
    def wyswietl_pole(self):
        print("Pole prostokąta o bokach ",self.a," i ", self.b," jest równe: ", self.pole())
    def wyswietl_obwod(self):
        print("Obwód prostokąta o bokach ",self.a," i ", self.b," jest równe: ", self.obwod())

class Osoba:
    def __init__(self,imie, nazwisko, wzrost, waga):
        self.im=imie
        self.naz=nazwisko
        self.wzr=wzrost
        self.wag=waga
    def przywitaj(self):
        print("Witaj ",self.im,self.naz)
    def informacje(self):
        print("Imię i nazwisko ", self.im,self.naz)
        print("Wzrost: ",self.wzr)
        print("Waga: ", self.wag)

class Trojkat:
    def __init__(self, a, b, c, wysokosc):
        self.pierwszy = a
        self.drugi = b
        self.trzeci = c
        self.wys = wysokosc
    def obwod(self):
        print(self.pierwszy+self.drugi+self.trzeci)
    def pole(self):
        print((self.pierwszy*self.wys)/2)

# prostokat1 = Prostokat(2,5)
# print("Pole wynosi: ",prostokat1.pole())
# print("Obwód wynosi: ",prostokat1.obwod())
#
# prostokat2 = ProstokatExtra(1,2)
# prostokat2.wyswietl_pole()
# prostokat2.wyswietl_obwod()
#
#
# a = int(input())
# b = int(input())
# prostokat3 = ProstokatExtra(a,b)
# prostokat3.wyswietl_pole()
# prostokat3.wyswietl_obwod()

# imie = input()
# nazwisko = input()
# wzrost = int(input())
# waga = int(input())
# osoba1 = Osoba(imie,nazwisko,wzrost,waga)
# print()
# osoba1.przywitaj()
# osoba1.informacje()

# a = int(input())
# b = int(input())
# c = int(input())
# wysokosc = int(input())
# trojkat1 = Trojkat(a,b,c, wysokosc)
# trojkat1.obwod()
# trojkat1.pole()

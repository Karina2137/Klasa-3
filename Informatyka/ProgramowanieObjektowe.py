#Zad.2
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


prostokat1 = Prostokat(2,5)
print("Pole wynosi: ",prostokat1.pole())
print("Obwód wynosi: ",prostokat1.obwod())

prostokat2 = ProstokatExtra(1,2)
prostokat2.wyswietl_pole()
prostokat2.wyswietl_obwod()


a = int(input())
b = int(input())
prostokat3 = ProstokatExtra(a,b)
prostokat3.wyswietl_pole()
prostokat3.wyswietl_obwod()

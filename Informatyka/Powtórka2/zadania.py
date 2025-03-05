#zad.2
wsp = list(map(int, input("Podaj ciąg liczb: ").split()))
x = int(input("Podaj x: "))
print(wsp, x)
n = len(wsp)
w = wsp[n-1]
for i in range(n-2, -1, -1):
    w=w*x+wsp[i]
print(w)

#zad.4
plik = open("liczby.txt", "r")
ciag = list(map(int, plik.readline().split()))
plik.close()
print(ciag)
dl = 1
dl_max = 1
n = len(ciag)
for i in range(1,n):
    if ciag[i-1] <= ciag[i]:
        dl+=1
    else:
        if dl > dl_max:
            dl_max = dl
        dl=1
if dl > dl_max:
    dl_max = dl
print(dl_max)

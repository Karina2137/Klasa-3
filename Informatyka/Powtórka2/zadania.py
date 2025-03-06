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

#zad.6
# with open("ciag.txt", "r") as file:
#     ciag = list(map(int, file.read().split()))
# # #ciag = ciag[:5]
# print(ciag)
# n = len(ciag)
# max_suma = ciag[0]
# for pocz in range(n):
#     for dl in range(1, n-pocz+1):
#         suma = sum(ciag[pocz:pocz+dl])
#         # #print(ciag[pocz:pocz + dl], suma)
#         if suma>max_suma:
#             max_suma=suma
# print(max_suma)

# #zad.5
# plik = open("ciag.txt", "r")
# ciag = list(map(int, plik.read().split()))
# plik.close()
# ciag = ciag[:5]
# n=len(ciag)
# max_suma=ciag[0]+ciag[1]+ciag[2]
# for pocz in range(1,n-2):
#     print(pocz)
#     for i in range(3):
#         print(ciag[pocz+i:3])
#         suma =+ciag[pocz+i]

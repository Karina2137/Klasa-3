# #zad.1
A = list(map(int, input("Podaj współczynniki od a0 do an: ").split()))
x = float(input("Podaj x: "))
n = len(A)-1
y = A[0]
potęga = 1
for i in range(1,n+1):
    potęga *= x
    y = y + A[i] * potęga
print(y)

#zad.2
B = list(map(int, input("Podaj współczynniki od a0 do an: ").split()))
a = float(input("Podaj x: "))
n = len(B)-1
b = B[0]
for i in range(n-1,-1,-1):
    b = a*b+B[i]
    print(b)
print()
print(b)

#zad.3
def Schemat_Hornera(A,x):
    n = len(A)-1
    if n==0:
        return A[0]
    return x * Schemat_Hornera(A[1:], x) + A[0]
B = list(map(int, input("Podaj współczynniki od a0 do an: ").split()))
a = float(input("Podaj x: "))
w = Schemat_Hornera(B,a)
print(w)

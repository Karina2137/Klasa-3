import random

Liczby = [random.randint(1, 1000) for _ in range(100)]
print(Liczby)

# Zad.1
# maximum = minimum = Liczby[0]
# n=len(Liczby)
# for i in range(1,n):
#     if Liczby[i]<minimum:
#         minimum=Liczby[i]
#     if Liczby[i]>maximum:
#         maximum=Liczby[i]
# print(minimum, maximum)
# wykonanych porównań 2*99=198

# Zad.2
# Liczba powtórzeń:
# 1+((n-2)/2)*3 = 1+(3/2)*(n-2)=1+(3/2)n-3=(3/2)n-2

# Zad.3
# n = len(Liczby)
# if Liczby[0]<Liczby[1]:
#     minimum = Liczby[0]
#     maximum = Liczby[1]
# else:
#     minimum = Liczby[1]
#     maximum = Liczby[0]
# for i in range(2,n-1,2):
#     if Liczby[i]<Liczby[i+1]:
#         if Liczby[i]<minimum:
#             minimum=Liczby[i]
#         if Liczby[i+1]>maximum:
#             maximum=Liczby[i+1]
#     else:
#         if Liczby[i+1]<minimum:
#             minimum=Liczby[i+1]
#         if Liczby[i]>maximum:
#             maximum=Liczby[i]

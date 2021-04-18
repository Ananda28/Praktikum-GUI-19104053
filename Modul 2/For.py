# Menggunakan Variable
angka = 10

# Param 1 : Maksimal
for i in range(angka) :
    print("Angka Ke : ")
    print(i)

# Param 2 : Minim, Maks
for i in range(angka, 20) :
    print("Angka Ke : ")
    print(i)

# Param 3 : Minim, Maks, Lompatan(decre,incre)
for i in range(angka, 1, -1) :
    print("Angka Ke : ")
    print(i)

#Array
array = [1,2,3,4]
for i in array :
    print(i, end = ' ')
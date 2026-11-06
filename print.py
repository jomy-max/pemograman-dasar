import math
print("1. Menghitung Keliling Lingkaran")
print("2. Menghitung Luas Lingkaran")
pilihan = int(input("Masukan pilihan (1/2): "))
r = float(input("Masukan jari-jari: "))

if pilihan == 1:
    keliling = 2 * math.pi * r
    print("Keliling lingkaran =", keliling)
elif pilihan == 2:
    luas = math.pi * r * r
    print("Luas lingkaran =", luas)
else:
    print("pilihan tidak valid! Masukan 1 atau 2 saja.")
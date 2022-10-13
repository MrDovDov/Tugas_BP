print("nama : Dian syamdova")
print("NIM : 20210801052")
print("Tugas Bahasa Pemogroman")
print("================")
# tertambahan


def tambah():
    a = 10
    b = 5
    c = a+b
    print(c)


tambah()

# pengurangan


def kurang():
    a = 10
    b = 5
    c = a-b
    print(c)


kurang()

# perkalian


def kali():
    a = 10
    b = 5
    c = a*b
    print(c)


kali()

# pembagian


def bagi():
    a = 10
    b = 5
    c = a/b
    print(c)


bagi()

print("Penjumlahan matriks ordo 2x2")

matriks1 = [[1, 2], [3, 4]]
matriks2 = [[5, 6], [7, 8]]
for x in range(0, len(matriks1)):
    for y in range(0, len(matriks1[0])):
        print(matriks1[x][y] + matriks2[x][y], end='')
    print('')
print("================")
print("Terima Kasih")
def nama():
    nim = 20210801052
    nama ="Dian syamdova"
    print("NIM :",nim)
    print("NAMA :",nama)
    print("=====================")

def menu():
    a = "capucino"
    b = "teh"
    print ("Pilihan")
    print ("1.", a)
    print ("2.", b)
    print ("3. Exit")

def capucino():
    cap = "memilih capucino"
    print(cap)
    capucino = int(input("masukkan harga : "))
    ppn = 10/100
    pajak = capucino*ppn
    total = capucino+pajak
    print("jumlah yang harus dibayar : ",total)
    

def teh():
    teh = "memilih TEH"
    print(teh)
    teh = int(input("masukkan harga : "))
    ppn = 10/100
    pajak = teh*ppn
    total = teh+pajak
    print("jumlah yang harus dibayar : ",total)

while True:
    nama()
    menu()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")
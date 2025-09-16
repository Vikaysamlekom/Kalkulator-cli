def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Tidak bisa bagi nol!"

while True:
    print("\n=== Kalkulator CLI ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Pilih operasi (1/2/3/4/5): ")

    if pilihan == "5":
        print("Terima kasih!")
        break

    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        print("Hasil:", tambah(a, b))
    elif pilihan == "2":
        print("Hasil:", kurang(a, b))
    elif pilihan == "3":
        print("Hasil:", kali(a, b))
    elif pilihan == "4":
        print("Hasil:", bagi(a, b))
    else:
        print("Pilihan tidak valid.")
 
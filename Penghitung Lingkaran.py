print("------------------------")
print("I Penghitung Lingkaran I")
print("------------------------\n")
print("=========+++=========")
print("1. Jari-Jari\n2. Keliling\n3. Luas")
print("=========+++=========\n")
pilihan = input("Pilih variabel yang diketahui: ")

# Contoh...   jari: 7, kel: 44, luas:154

if pilihan == "1":
    jari = float(input("\nKetik Jari-Jari: "))
    kel = round(jari * 2 * (22 / 7), 2)
    luas = round(jari ** 2 * (22 / 7), 2)
    print("\nKeliling: " + str(kel), "Luas: " + str(luas))
    input('\nTekan "Enter" untuk mengakhiri')

elif pilihan == "2":
    kel = float(input("\nKetik Keliling: "))
    jari = round(kel / (22 / 7) / 2, 2)
    luas = round(jari ** 2 * (22 / 7), 2)
    print("\nJari-Jari: " + str(jari), "Luas: " + str(luas))
    input('\nTekan "Enter" untuk mengakhiri')

elif pilihan == "3":
    luas = float(input("\nKetik Luas: "))
    jari = round((luas / (22 / 7))**.5, 2)
    kel = round(jari * 2 * (22 / 7), 2)
    print("\nJari-Jari: " + str(jari), "Keliling: " + str(kel))
    input('\nTekan "Enter" untuk mengakhiri')

else:
    print("\nPilih 1/2/3 TOLOL")
    input('\nTekan "Enter" untuk mengakhiri')


while True:
    print ("pilih menu")
    print ("1.Penambahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\nQ.Keluar")
    pilih = input("masukkan pilihan:")
    
    if pilih == "1":
        bil1 = int(input("masukkan bilangan pertama: "))
        bil2 = int(input("masukkan bilangan kedua: "))
        hasil = bil1 + bil2
        print("hasilnya adalah: ", hasil)
    elif pilih == "2":
        bil1 = int(input("masukkan bilangan pertama: "))
        bil2 = int(input("masukkan bilangan kedua: "))
        hasil = bil1 - bil2
        print("hasilnya adalah: ", hasil)
    elif pilih == "3":
        bil1 = int(input("masukkan bilangan pertama: "))
        bil2 = int(input("masukkan bilangan kedua: "))
        hasil = bil1 * bil2
        print("hasilnya adalah: ", hasil)
    elif pilih == "4":
        bil1 = int(input("masukkan bilangan pertama: "))
        bil2 = int(input("masukkan bilangan kedua: "))
        hasil = bil1 / bil2
        print("hasilnya adalah: ", hasil)
    elif pilih == "Q":
        break

    
    
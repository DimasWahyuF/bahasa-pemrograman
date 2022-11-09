NIM = input("Masukan NIM :")
Nama = input("Masukan Nama:")

menu = "y" or "Y"

while menu == "y" or "Y":
    print(" 1. Cappucino")
    print(" 2. Teh")
    print(" 3. Exit")
    listMenu=str(input(" Masukkan Pilihan = "))
    
    if listMenu == "1":
        print("Memilih Cappucino")
        namaMenu= " Cappucino"
    elif listMenu == "2":
        print("Memilih Teh")
        namaMenu= " Teh"
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di restoran")
        
        
    harga=int(input(" Masukan harga = "))
    
    if listMenu == "1":
        pajak= int(harga * 0.1)
        totalHarga=int(harga+pajak)
    elif listMenu == "2":
        pajak = int(harga * 0.1)
        totalHarga =int(harga+pajak)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di restoran")
    print(" ------------------------------")
    print(" Total Yang Harus dibayarkan :", totalHarga +.0)
    print(" ------------------------------")
    break
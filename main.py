print(f"{'daftar menu rm yusuf bahari'.upper():>30}")
print(f"{'Jln. Agung raya No.254'.upper():>30}")
print("========================================")
print()

menu1: str = "Ikan kerapu bakar"
menu2: str = "Ikan kakap merah gulai"
menu3: str = "Ikan cakalang bakar"
menu4: str = "Kepiting lada hitam"
menu5: str = "Es teler"
harga1: int = 48000
harga2: int = 55000
harga3: int = 32000
harga4: int = 52000
harga5: int = 12000

print(f"|{'No':^5}|{'Pesanan':^12}|{'Harga':^10}|")
print("================================")
print(f"|{1:^5}|{menu1:^12}|{harga1:^10}")
print(f"|{2:^5}|{menu2:^12}|{harga2:^10}")
print(f"|{3:^5}|{menu3:^12}|{harga3:^10}")
print(f"|{4:^5}|{menu4:^12}|{harga4:^10}")
print(f"|{5:^5}|{menu5:^12}|{harga5:^10}")
print()

# INPUT OUTPUT
while True:
    print("PILIH AKSI >>")
    print("1. Beli")
    print("2. Lihat Keranjang")
    print("3. Edit")
    print("4. Hapus")
    print("5. Exit")

    aksi = input("Pilih aksi [1-5] : ")

    # 1. BELI
    if aksi == "1":
        print("\nDAFTAR MENU")
        daftar_menu = {
            menu1: harga1,
            menu2: harga2,
            menu3: harga3,
            menu4: harga4,
            menu5: harga5
        }
        keranjang = {}
        for nomor, (nama, harga) in enumerate(
            daftar_menu.items(), start=1
        ):
            print(f"{nomor}. {nama:<25} Rp {harga:,}")
        nama_input = input("\nInput Menu: ")
        if nama_input in daftar_menu:
            jumlah = int(input("Input Pembelian [min 1] : "))
            if jumlah < 1:
                print("Jumlah pembelian minimal 1!")
                continue
            harga_item = daftar_menu[nama_input]
            subtotal = harga_item * jumlah
            keranjang[nama_input] = (
                keranjang.get(nama_input, 0) + jumlah
            )
            print(f"Harga Item   : Rp {harga_item:,}")
            print(f"Sub Total    : Rp {subtotal:,}")
            uang = int(input("Input Uang   : Rp "))
            if uang >= subtotal:
                kembalian = uang - subtotal
                print(f"Kembalian    : Rp {kembalian:,}")
                print("... Makasih cuy ...")
            else:
                print("Uang kurang!")
                print("Pesanan tetap masuk keranjang.")
        else:
            print("Menu tidak ditemukan!")
    # 5. EXIT
    elif aksi == "5":
        print("... Terima kasih ...")
        break
    else:
        print("Pilihan tidak tersedia.")
    print()
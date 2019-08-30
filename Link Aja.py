def menu():
    print("\n1.Cek Saldo\n2.TopUp Saldo\n3.Pembelian")
    pilih = input("Pilih Menu = ")

    if pilih == "1":
        cek()
    if pilih == "2":
        top()
    if pilih == "3":
        pem()
    else:
        print("\n-----------------------------TIDAK ADA MASUKAN-----------------------------\n")

def cek():
    sld = 1500000
    print("Jumlah Saldo Anda = Rp. ",sld)
    tanya()

def top():
    sld = 1500000          
    print("Saldo Akhir = ",sld)
    jml_top = int(input("Jumlah TopUp = "))
    hsl = sld+jml_top
    print("Jumlah Saldo Setelah TOPUP = ",hsl)
    tanya()   

def pem():
    sld = 1500000
    str(input("\nNama Barang = "))
    print("Jumlah Saldo = ",sld)
    hrgbrg = int(input("Harga Barang = "))
    jmlbrg = eval(input("Jumlah Barang = "))
    peng = hrgbrg*jmlbrg 
    print("Total Harga = ",peng)
    if peng > sld:
        print("Silahkan TopUP Terlebih dahulu")
    if peng < sld:
        print("Transaksi Berhasil")
    tanya()

def tanya():   
    print("\nY.Kembali\nT.Keluar")
    plh = input("[Y/T] = ")
    if plh == "Y":
        menu()
    if plh == "T":
        print("---------------------------------THANK YOU---------------------------------")
menu()
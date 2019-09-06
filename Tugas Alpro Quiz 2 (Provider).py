print("\nGiveaway Mahasiswa Telkom University\n")
    
    
krt = str(input("Kartu = "))
ip = float(input("IPK = "))
name = str(input("Mahasiswa = "))

if krt == "Telkomsel" and ip > 3:
    print(name, "Selamat Anda Mendapatkan Iphone X")

elif krt != "Telkomsel" and ip > 3:
    print(name, "Selamat anda mendapatkan HP Samsung J Galaxy")

elif krt == "Telkomsel" and 2.5 <= ip <= 3:
    print(name, "Selamat anda mendapatkan Playstation 4")

elif krt !="Telkomsel" and 2.5 <= ip <= 3:
    print(name, "Selamat anda mendapatkan voucher menginap di IBIS Hotel")
 
elif krt == "Telkomsel" and ip == 2 < 2.5:
    print(name, "Selamat anda mendapatkan voucher menginap di pondok pesantren Darul Tauhid")

elif krt != "Telkomsel" and ip == 2 <= 2.5:
    print(name, "Selamat anda mendapatkan voucher ke klinik sikologi")

else:
    print ("\nSelamat Dan Terimakasih", name), print("Anda Tidak Memenuhi Syarat Giveaway\n")
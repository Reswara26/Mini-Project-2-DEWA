print("""
=======================================
Nama    : Reswara Ganendra Rashi Dewa
NIM     : 2409116100
Kelas   : Sistem Infromasi C '2024
MINI PROJECT 2 DASAR PEMROGRAMAN
=======================================
""")

from prettytable import PrettyTable

ketersediaan_mobil = {
    1: {"merek": "BMW", "tipe": "X5", "harga": 1200000000},
    2: {"merek": "BMW", "tipe": "M3", "harga": 1500000000},
    3: {"merek": "BMW", "tipe": "i8", "harga": 2000000000},
    4: {"merek": "BMW", "tipe": "X3", "harga": 1000000000},
    5: {"merek": "BMW", "tipe": "M4", "harga": 2400000000}
}

def create_mobil():
    print("\n|| Tambah Mobil ||")
    tabel = PrettyTable()
    tabel.title = "LIST MOBIL YANG TERSEDIA"
    tabel.field_names = ["Nomor", "Merek", "Tipe", "Harga"]
    for nomor, data_mobil in ketersediaan_mobil.items():
        tabel.add_row([nomor, data_mobil["merek"], data_mobil["tipe"], data_mobil["harga"]])
    print(tabel)
    nomor_mobil = len(ketersediaan_mobil) + 1
    merek = "BMW"
    tipe = input("Masukkan Tipe Mobil: ")
    harga = int(input("Masukkan Harga Mobil: "))
    ketersediaan_mobil[nomor_mobil] = {"merek": merek, "tipe": tipe, "harga": harga}
    print("Mobil Berhasil Ditambahkan!")

def read_mobil():
    tabel = PrettyTable()
    tabel.title = "LIST MOBIL YANG TERSEDIA"
    tabel.field_names = ["Nomor", "Merek", "Tipe", "Harga"]
    for nomor, data_mobil in ketersediaan_mobil.items():
        tabel.add_row([nomor, data_mobil["merek"], data_mobil["tipe"], data_mobil["harga"]])
    print(tabel)

def update_mobil():
    print("\n|| Memperbarui Mobil ||")
    read_mobil()
    while True :
        if ketersediaan_mobil:
            try:
                nomor_mobil = int(input("Masukkan Nomor Mobil yang Ingin Diupdate: "))
                if nomor_mobil in ketersediaan_mobil:
                    tipe = input("Masukkan Tipe Baru: ")
                    harga = int(input("Masukkan Harga Baru: "))
                    ketersediaan_mobil[nomor_mobil] = {"merek": "BMW", "tipe": tipe, "harga": harga}
                    print("\nData Mobil Berhasil Diperbarui!")
                    break
                else:
                    print("*!* Nomor Mobil Tidak Ditemukan! *!*")
            except Exception as e:
                print(f"*!* Error pada {e}! *!*")
            except KeyboardInterrupt:
                print("*!* Jangan Pencet CTRL + C *!*")

def delete_mobil():
    print("|| Menghapus Mobil ||")
    read_mobil()
    while True:
        if ketersediaan_mobil:
            try:
                nomor_mobil = int(input("Masukkan Nomor Mobil yang Ingin Dihapus: "))
                if nomor_mobil in ketersediaan_mobil:
                    del ketersediaan_mobil[nomor_mobil]
                    print("Mobil Berhasil Dihapus!")
                    break
                else:
                    print("*!* Nomor Mobil Tidak Ditemukan! *!*")
            except Exception as e:
                print(f"*!* Error pada {e}! *!*")
            except KeyboardInterrupt:
                print("*!* Jangan Pencet CTRL + C *!*")

def beli_mobil():
    read_mobil()
    while True:
        if ketersediaan_mobil:
            try:
                nomor_mobil = int(input("Masukkan Nomor Mobil yang Ingin Dibeli: "))
                if nomor_mobil in ketersediaan_mobil:
                    mobil = ketersediaan_mobil[nomor_mobil]
                    print(f"\nAnda memilih {mobil['merek']} {mobil['tipe']} dengan harga {mobil['harga']}")
                    bayar = input("Apakah Anda Ingin Melanjutkan Pembayaran? (y/n): ")
                    if bayar.lower() == "y":
                        print("Pembayaran Berhasil! Terima Kasih! Silakan Menikmati Mobil BMW Baru Anda!")
                        del ketersediaan_mobil[nomor_mobil]
                        break
                    elif bayar.lower() == "n":
                        print("Pembayaran Dibatalkan.")
                        break
                    else:
                        print("*!* Input Tidak Sesuai! Periksa Kembali Pilihan Anda. *!*")
                else:
                    print("*!* Nomor Mobil Tidak Ditemukan! *!*")
            except Exception as e:
                print(f"*!* Error pada {e}! *!*")
            except KeyboardInterrupt:
                print("*!* Jangan Pencet CTRL + C *!*")

def sebagai_admin():
    print("\n========== MEMASUKI BAGIAN ADMIN ==========")
    while True:
        print("""
        [1]. Tambah Mobil
        [2]. Lihat Daftar Mobil
        [3]. Update Mobil
        [4]. Hapus Mobil
        [5]. Log Out
        """)
        try:
            pilihan = int(input("Masukkan Pilihan Menu: "))
            if pilihan == 1:
                create_mobil()
            elif pilihan == 2:
                read_mobil()
            elif pilihan == 3:
                update_mobil()
            elif pilihan == 4:
                delete_mobil()
            elif pilihan == 5:
                print("Keluar dari Program Admin.")
                exit()
            else:
                print("*!* Pilihan Menu Tidak Ditemukan! Silakan Periksa Kembali Pilihan Anda! *!*")
        except Exception as e:
            print(f"*!* Error pada {e}! *!*")
        except KeyboardInterrupt:
            print("*!* Jangan Pencet CTRL + C *!*")

def sebagai_pembeli():
    print("\n========== MEMASUKI BAGIAN PEMBELI ==========")
    while True:
        print("""
        [1]. Lihat Daftar Mobil
        [2]. Pilih dan Bayar Mobil
        [3]. Log Out
        """)
        try:
            pilihan = int(input("Masukkan Pilihan Menu: "))
            if pilihan == 1:
                read_mobil()
            elif pilihan == 2:
                beli_mobil()
            elif pilihan == 3:
                print("Keluar dari Program Pembeli.")
                exit()
            else:
                print("*!* Pilihan Menu Tidak Ditemukan! Silakan Periksa Kembali Pilihan Anda! *!*")
        except Exception as e:
            print(f"*!* Error pada {e}! *!*")
        except KeyboardInterrupt:
            print("*!* Jangan Pencet CTRL + C *!*")

def login():
    print("========== LAKUKAN LOGIN TERLEBIH DAHULU ==========")
    usernameAdmin = "DEWAADMIN"
    pwAdmin = "admin2024"
    usernamePembeli = "DEWAPEMBELI"
    pwPembeli = "pembeli2024"
    while True:
        username1 = str(input("Masukkan Username : "))
        pw1 = str(input("Masukkan Password : "))
        if username1 == usernameAdmin and pw1 == pwAdmin:
            print("Berhasil Masuk Sebagai ADMIN! Selamat Datang DEWA!")
            sebagai_admin()
        elif username1 == usernamePembeli and pw1 == pwPembeli:
            print("Berhasil Masuk Sebagai PEMBELI! Selamat Datang DEWA!")
            sebagai_pembeli()
        else:
            print("*!* User atau Password Salah, Periksa Kembali Input Anda. *!*")

login()
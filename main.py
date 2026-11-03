import os
import time
import json
from prettytable import PrettyTable
from pwinput import pwinput
import random

# Untuk Bersihkan Terminal
def bersih():   
    os.system("cls")

# Untuk Input Biar Tidak Error Saat Ctrl + C
def asalpicik(pesan):
    while True:
        try:
            return input(pesan)
        except KeyboardInterrupt:
            print("\nNo No Yaa!\n")
        except EOFError:
            print("\nNo No Yaa!")

# Menu Utama 
def menu_utama():
    while True:
        bersih()
        print("================================================================")
        print("|                           Menu Utama                         |")
        print("================================================================")
        print("| 1. Registrasi                                                |")
        print("| 2. Login                                                     |")
        print("| 3. Keluar Aplikasi                                           |")
        print("================================================================")
        pilihan = asalpicik(("Pilih menu: "))
        if pilihan == "1":
            registrasi()
            asalpicik("\nTekan Enter Untuk Melanjutkan ")
        elif pilihan == "2":
            login()
            asalpicik("\nTekan Enter untuk kembali ke menu utama ")
        elif pilihan == "3":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak tersedia")
            time.sleep(1)

# Registrasi
def registrasi():
    bersih()
    print("================================================================")   
    print("|                          Registrasi                          |")
    print("================================================================")

    with open("user.json", "r") as file:
        users = json.load(file)

    while True:
        try:
            username =  asalpicik("Masukkan username: ").strip()
            if username == "":
                raise ValueError("Username tidak boleh kosong....")
            if len(username) < 5:
                raise ValueError("Username minimal 5 karakter....")
            username_dipakai = False
            for akun in users:
                if akun["username"].lower() == username.lower():
                    username_dipakai = True
                    break
            if username_dipakai:
                print("Username sudah digunakan, Silakan masukkan username lain.")
            else:
                break
        except ValueError as e:
            print(e)
    while True:
        try:
            password = pwinput("Masukkan password: ")

            if password == "":
                raise ValueError("Password tidak boleh kosong....")

            if len(password) < 5:

                raise ValueError("Password minimal 5 karakter....")
            break
        except ValueError as e:
            print(e)

    akun_baru = {
        "username": username,
        "password": password,
        "role": "user",
        "saldo": 0
    }

    users.append(akun_baru)

    with open("user.json", "w") as file:
        json.dump(users, file, indent=4)

    print("\nRegistrasi berhasil!")
    time.sleep(1)

# Login
def login():
    try:
        with open("user.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    except json.JSONDecodeError:
        print("File user.json tidak valid")
        return
    kesempatan = 3
    while kesempatan > 0:
        bersih()
        print("================================================================")
        print("|                          Login                               |")
        print("================================================================")
        username = asalpicik(("Username: ")).strip()
        password = pwinput("Password: ")
        akun_ditemukan = None
        for akun in users:
            if akun["username"].lower() == username.lower():
                akun_ditemukan = akun
                break
        if akun_ditemukan is not None:
            if akun_ditemukan["password"] == password:
                print("Login berhasil!")
                time.sleep(1)
                if akun_ditemukan["role"] == "admin":
                    menu_admin()
                else:
                    menu_user(akun_ditemukan["username"])
                return
        kesempatan -= 1
        print("Username atau password salah!")
        if kesempatan > 0:
            print("Sisa percobaan:", kesempatan)
            time.sleep(1)
        else:
            print("Batas percobaan login tercapai.")
            time.sleep(2)

# Menampilkan Barang
def tampilkan_barang():
    bersih()
    try:
        with open("barang.json", "r") as file:
            barang = json.load(file)
    except FileNotFoundError:
        barang = []
    except json.JSONDecodeError:
        print("File barang.json tidak valid.")
        return

    print("================================================================")
    print("|                       Daftar Barang                          |")
    print("================================================================")

    if not barang:
        print("Belum ada barang tersedia.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Barang", "Harga", "Stok"]
    for item in barang:
        tabel.add_row([
            item["no"],
            item["nama"],
            "Rp" + format(item["harga"], ","),
            item["stok"]
        ])

    print(tabel)

# Menambah Barang (Admin)
def tambah_barang():
    bersih()

    try:
        with open("barang.json", "r") as file:
            barang = json.load(file)
    except FileNotFoundError:
        barang = []
    except json.JSONDecodeError:
        print("File barang.json tidak valid.")
        return

    print("================================================================")
    print("|                       Tambah Barang                          |")
    print("================================================================")

    id_barang = asalpicik(("No barang: ")).strip().upper()

    if not id_barang:
        print("No barang tidak boleh kosong.")
        return

    for item in barang:
        if item["no"].upper() == id_barang:
            print("No barang sudah digunakan.")
            return

    nama = asalpicik(("Nama barang: ")).strip()

    if not nama:
        print("Nama barang tidak boleh kosong.")
        return

    while True:
        try:
            harga = int(asalpicik(("Harga barang: Rp")))

            if harga < 1:
                print("Harga minimal Rp1.")
            else:
                break

        except ValueError:
            print("Input harus berupa angka bulat!")

    while True:
        try:
            stok = int(asalpicik(("Stok barang: ")))

            if stok < 0:
                print("Stok tidak boleh negatif.")
            else:
                break

        except ValueError:
            print("Input harus berupa angka bulat!")

    barang.append({
        "no": id_barang,
        "nama": nama,
        "harga": harga,
        "stok": stok
    })

    with open("barang.json", "w") as file:
        json.dump(barang, file, indent=4)

    print("Barang berhasil ditambahkan.")

# Mengubah Barang (Admin)
def ubah_barang():
    bersih()

    try:
        with open("barang.json", "r") as file:
            barang = json.load(file)
    except FileNotFoundError:
        print("File barang.json tidak ditemukan.")
        return
    except json.JSONDecodeError:
        print("File barang.json tidak valid.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Barang", "Harga", "Stok"]

    for item in barang:
        tabel.add_row([
            item["no"],
            item["nama"],
            "Rp" + format(item["harga"], ","),
            item["stok"]
        ])

    print(tabel)

    id_barang = asalpicik(("No barang yang ingin diubah: ")).strip().upper()
    item_ditemukan = None

    for item in barang:
        if item["no"].upper() == id_barang:
            item_ditemukan = item
            break

    if item_ditemukan is None:
        print("Barang tidak ditemukan.")
        return

    print("Kosongkan input jika tidak ingin mengubah data.")

    nama = asalpicik(("Nama baru: ")).strip()

    if nama:
        item_ditemukan["nama"] = nama

    while True:
        jawaban = asalpicik(("Ubah harga? (y/n): ")).lower()

        if jawaban == "y" or jawaban == "n":
            break

        print("Masukkan y atau n.")

    if jawaban == "y":
        while True:
            try:
                harga = int(asalpicik(("Harga baru: Rp")))

                if harga < 1:
                    print("Harga minimal Rp1.")
                else:
                    item_ditemukan["harga"] = harga
                    break

            except ValueError:
                print("Input harus berupa angka bulat!")

    while True:
        jawaban = asalpicik(("Ubah stok? (y/n): ")).lower()

        if jawaban == "y" or jawaban == "n":
            break

        print("Masukkan y atau n.")

    if jawaban == "y":
        while True:
            try:
                stok = int(asalpicik(("Stok baru: ")))

                if stok < 0:
                    print("Stok tidak boleh negatif.")
                else:
                    item_ditemukan["stok"] = stok
                    break

            except ValueError:
                print("Input harus berupa angka bulat!")

    with open("barang.json", "w") as file:
        json.dump(barang, file, indent=4)

    print("Data barang berhasil diperbarui.")

# Menghapus Barang (Admin)
def hapus_barang():
    bersih()

    try:
        with open("barang.json", "r") as file:
            barang = json.load(file)
    except FileNotFoundError:
        print("File barang.json tidak ditemukan.")
        return
    except json.JSONDecodeError:
        print("File barang.json tidak valid.")
        return

    if not barang:
        print("Belum ada barang tersedia.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Barang", "Harga", "Stok"]

    for item in barang:
        tabel.add_row([
            item["no"],
            item["nama"],
            "Rp" + format(item["harga"], ","),
            item["stok"]
        ])

    print(tabel)

    id_barang = asalpicik(("No barang yang ingin dihapus: ")).strip().upper()
    item_ditemukan = None

    for item in barang:
        if item["no"].upper() == id_barang:
            item_ditemukan = item
            break

    if item_ditemukan is None:
        print("Barang tidak ditemukan.")
        return

    while True:
        jawaban = asalpicik((
            "Hapus " + item_ditemukan["nama"] + "? (y/n): "
        )).lower()

        if jawaban == "y":
            barang.remove(item_ditemukan)
            break

        elif jawaban == "n":
            print("Penghapusan dibatalkan.")
            return

        else:
            print("Masukkan y atau n.")

    with open("barang.json", "w") as file:
        json.dump(barang, file, indent=4)

    print("Barang berhasil dihapus.")

# Menu Kelola Barang (Admin)
def menu_crud_barang():
    while True:
        bersih()

        print("================================================================")
        print("|                       Kelola Barang                          |")
        print("================================================================")
        print("| 1. Tampilkan barang                                          |")
        print("| 2. Tambah barang                                             |")
        print("| 3. Ubah barang                                               |")
        print("| 4. Hapus barang                                              |")
        print("| 5. Kembali                                                   |")
        print("================================================================")

        pilihan = asalpicik("Pilih menu: ")

        if pilihan == "1":
            tampilkan_barang()

        elif pilihan == "2":
            tambah_barang()

        elif pilihan == "3":
            ubah_barang()

        elif pilihan == "4":
            hapus_barang()

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak tersedia.")

        if pilihan != "5":
            asalpicik("\nTekan Enter untuk melanjutkan...")


# Buat Cetak Invoice
def cetak_invoice(data):
    tabel = PrettyTable()
    tabel.field_names = ["Keterangan", "Detail"]

    tabel.add_row(["Kode Transaksi", data["kode"]])
    tabel.add_row(["Waktu", data["waktu"]])
    tabel.add_row(["Username", data["username"]])
    tabel.add_row(["Jenis", data["jenis"]])
    tabel.add_row(["Detail", data["detail"]])
    tabel.add_row([
        "Total",
        "Rp" + format(data["total"], ",")
    ])
    tabel.add_row([
        "Sisa Saldo",
        "Rp" + format(data["saldo_setelah"], ",")
    ])

    print("\n============ Invoice ============")
    print(tabel)
    print("=================================")

# Top Up
def top_up(username):
    bersih()

    try:
        with open("user.json", "r") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Data pengguna tidak tersedia atau tidak valid.")
        return

    try:
        with open("transaksi.json", "r") as file:
            transaksi = json.load(file)
    except FileNotFoundError:
        transaksi = []
    except json.JSONDecodeError:
        print("File transaksi.json tidak valid.")
        return

    akun = None

    for data_akun in users:
        if data_akun["username"].lower() == username.lower():
            akun = data_akun
            break

    if akun is None:
        print("Pengguna tidak ditemukan.")
        return

    print("================================================================")
    print("|                       Top Up Saldo                           |")
    print("================================================================")
    print("Saldo saat ini: Rp", format(akun["saldo"], ","))

    while True:
        try:
            jumlah = int(asalpicik("Nominal top up: Rp"))

            if jumlah < 1:
                print("Nominal minimal Rp1.")
            elif jumlah > 10000000:
                print("Nominal top up maksimal Rp10.000.000")    
            else:
                break
        except ValueError:        
            print("Input harus berupa angka bulat!")

    konfirtopup = asalpicik(f"Apakah Anda yakin ingin top up sebesar Rp {format(jumlah, ',')}? (y/n): ")
    if konfirtopup != "y":
        print("Top up dibatalkan.")
        return

    akun["saldo"] += jumlah
    with open("user.json", "w") as file:
        json.dump(users, file, indent=4)
    waktu = time.strftime("%Y-%m-%d")
    awalun = "TRX"
    angka_acak = str(random.randint(100, 999))
    nomor_urut = str(len(transaksi) + 1).zfill(3)
    kode = awalun + angka_acak + nomor_urut

    data = {
        "kode": kode,
        "username": akun["username"],
        "jenis": "TOP UP",
        "detail": "Top up saldo",
        "total": jumlah,
        "waktu": waktu,
        "saldo_setelah": akun["saldo"]
    }

    transaksi.append(data)

    with open("transaksi.json", "w") as file:
        json.dump(transaksi, file, indent=4)

    print("Top up berhasil!")
    cetak_invoice(data)

# Membeli Barang (User)
def beli_barang(username):
    bersih()

    try:
        with open("user.json", "r") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Data pengguna tidak tersedia atau tidak valid.")
        return

    try:
        with open("barang.json", "r") as file:
            barang = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Data barang tidak tersedia atau tidak valid.")
        return

    try:
        with open("transaksi.json", "r") as file:
            transaksi = json.load(file)
    except FileNotFoundError:
        transaksi = []
    except json.JSONDecodeError:
        print("File transaksi.json tidak valid.")
        return

    akun = None

    for data_akun in users:
        if data_akun["username"].lower() == username.lower():
            akun = data_akun
            break

    if akun is None:
        print("Pengguna tidak ditemukan.")
        return

    if not barang:
        print("Belum ada barang tersedia.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Barang", "Harga", "Stok"]

    for item in barang:
        tabel.add_row([
            item["no"],
            item["nama"],
            "Rp" + format(item["harga"], ","),
            item["stok"]
        ])

    print(tabel)

    id_barang = asalpicik("Masukkan No barang: ").strip().upper()
    item_ditemukan = None

    for item in barang:
        if item["no"].upper() == id_barang:
            item_ditemukan = item
            break

    if item_ditemukan is None:
        print("Barang tidak ditemukan.")
        return

    if item_ditemukan["stok"] <= 0:
        print("Stok barang habis.")
        return

    while True:
        try:
            jumlah = int(asalpicik("Jumlah pembelian: "))

            if jumlah < 1:
                print("Jumlah minimal 1.")
            elif jumlah > item_ditemukan["stok"]:
                print("Stok barang tidak mencukupi.")
            else:
                break

        except ValueError:
            print("Input harus berupa angka bulat!")

    total = item_ditemukan["harga"] * jumlah

    print("Nama barang:", item_ditemukan["nama"])
    print("Jumlah:", jumlah)
    print("Total: Rp", format(total, ","))
    print("Saldo: Rp", format(akun["saldo"], ","))

    if akun["saldo"] < total:
        print("Saldo tidak mencukupi. Silakan top up.")
        return

    while True:
        jawaban = asalpicik("Lanjutkan pembayaran? (y/n): ").lower()

        if jawaban == "y":
            break

        elif jawaban == "n":
            print("Pembelian dibatalkan.")
            return

        else:
            print("Masukkan y atau n.")

    akun["saldo"] -= total
    item_ditemukan["stok"] -= jumlah

    with open("user.json", "w") as file:
        json.dump(users, file, indent=4)

    with open("barang.json", "w") as file:
        json.dump(barang, file, indent=4)

    waktu = time.strftime("%Y-%m-%d")
    awalun = "TRX"
    angka_acak = str(random.randint(100, 999))
    nomor_urut = str(len(transaksi) + 1).zfill(3)
    kode = awalun + angka_acak + nomor_urut

    data = {
        "kode": kode,
        "username": akun["username"],
        "jenis": "PEMBELIAN",
        "detail": item_ditemukan["nama"] + " x " + str(jumlah),
        "total": total,
        "waktu": waktu,
        "saldo_setelah": akun["saldo"]
    }

    transaksi.append(data)

    with open("transaksi.json", "w") as file:
        json.dump(transaksi, file, indent=4)

    print("Pembelian berhasil!")
    cetak_invoice(data)

# Riwayat Transaksi
def riwayat_transaksi(username=None):
    bersih()
    try:
        with open("transaksi.json", "r") as file:
            transaksi = json.load(file)
    except FileNotFoundError:
        transaksi = []
    except json.JSONDecodeError:
        print("File transaksi.json tidak valid.")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "Kode", "Username", "Jenis",
        "Detail", "Total", "Waktu"
    ]

    ditemukan = False

    for data in transaksi:
        if username is None or data["username"] == username:
            tabel.add_row([
                data["kode"],
                data["username"],
                data["jenis"],
                data["detail"],
                "Rp" + format(data["total"], ","),
                data["waktu"]
            ])
            ditemukan = True
    if ditemukan:
        print(tabel)
    else:
        print("Belum ada transaksi.")

# Laporan Admin (Admin)
def laporan_admin():
    bersih()
    try:
        with open("transaksi.json", "r") as file:
            transaksi = json.load(file)
    except FileNotFoundError:
        transaksi = []
    except json.JSONDecodeError:
        print("File transaksi.json tidak valid.")
        return

    pendapatan = 0
    jumlah_transaksi = 0
    penjualan_barang = {}

    for data in transaksi:
        if data["jenis"] == "PEMBELIAN":
            pendapatan += data["total"]
            jumlah_transaksi += 1

            bagian = data["detail"].rsplit(" x ", 1)
            nama = bagian[0]
            jumlah = int(bagian[1])

            if nama in penjualan_barang:
                penjualan_barang[nama] += jumlah
            else:
                penjualan_barang[nama] = jumlah

    print("================================================================")
    print("|                     Laporan Penjualan                        |")
    print("================================================================")
    print("Total pendapatan: Rp", format(pendapatan, ","))
    print("Jumlah transaksi pembelian:", jumlah_transaksi)

    if penjualan_barang:
        terlaris = max(
            penjualan_barang,
            key=penjualan_barang.get
        )

        print("Produk terlaris:", terlaris)
        print("Jumlah terjual:", penjualan_barang[terlaris])
    else:
        print("Belum ada penjualan.")

# Tampilkan User (Admin)
def tampilkan_users():
    bersih()
    try:
        with open("user.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    except json.JSONDecodeError:
        print("File user.json tidak valid.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["Username", "Role", "Saldo"]
    for akun in users:
        if akun["role"].lower() == "user":
            tabel.add_row([
                akun["username"],
                akun["role"],
                "Rp " + format(akun["saldo"], ",")
        ])
    print(tabel)

# Menu Admin
def menu_admin():
    while True:
        bersih()
        print("================================================================")
        print("|                           Menu Admin                         |")
        print("================================================================")
        print("| 1. Kelola barang                                             |")
        print("| 2. Lihat pengguna                                            |")
        print("| 3. Lihat seluruh transaksi                                   |")
        print("| 4. Laporan penjualan                                         |")
        print("| 5. Logout                                                    |")
        print("================================================================")
        pilihan = asalpicik("Pilih menu: ")
        if pilihan == "1":
            menu_crud_barang()
        elif pilihan == "2":
            tampilkan_users()
        elif pilihan == "3":
            riwayat_transaksi()
        elif pilihan == "4":
            laporan_admin()
        elif pilihan == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak tersedia.")
        if pilihan != "5":
            asalpicik("\nTekan Enter untuk melanjutkan...")

# Menu User
def menu_user(username):
    while True:
        bersih()

        try:
            with open("user.json", "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Data pengguna tidak tersedia atau tidak valid.")
            return

        saldo = 0

        for akun in users:
            if akun["username"].lower() == username.lower():
                saldo = akun["saldo"]
                break
    
        print("================================================================")
        print("|                           Menu User                          |")
        print("================================================================")
        print(" Halo,", username,)
        print(" Saldo: Rp", format(saldo, ","))
        print("================================================================")
        print("| 1. Lihat barang                                              |")
        print("| 2. Top up saldo                                              |")
        print("| 3. Beli barang                                               |")
        print("| 4. Riwayat transaksi                                         |")
        print("| 5. Logout                                                    |")
        print("================================================================")
        pilihan = asalpicik("Pilih menu: ")
        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            top_up(username)
        elif pilihan == "3":
            beli_barang(username)
        elif pilihan == "4":
            riwayat_transaksi(username)
        elif pilihan == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak tersedia.")
        if pilihan != "5":
            asalpicik("\nTekan Enter untuk melanjutkan...")

# Inisialisasi Data Awal
def inisialisasi_data():
    data_user = [
        {
            "username": "admin",
            "password": "admin123",
            "role": "admin",
            "saldo": 0
        }
    ]

    data_barang = [
        {
            "no": "1",
            "nama": "PDH KBM FT",
            "harga": 165000,
            "stok": 20
        },
        {
            "no": "2",
            "nama": "Kaos FT",
            "harga": 100000,
            "stok": 50
        },
        {
            "no": "3",
            "nama": "Gantungan Kunci FT",
            "harga": 20000,
            "stok": 50
        },
        {
            "no": "4",
            "nama": "Slayer FT",
            "harga": 35000,
            "stok": 25
        },
        {
            "no": "5",
            "nama": "Sticker FT",
            "harga": 5000,
            "stok": 30
        },
        {
            "no": "6",
            "nama": "Kaos Kaki FT",
            "harga": 15000,
            "stok": 50
        }
    ]

    if not os.path.exists("user.json"):
        with open("user.json", "w") as file:
            json.dump(data_user, file, indent=4)

    if not os.path.exists("barang.json"):
        with open("barang.json", "w") as file:
            json.dump(data_barang, file, indent=4)

    if not os.path.exists("transaksi.json"):
        with open("transaksi.json", "w") as file:
            json.dump([], file, indent=4)

# Main Program  
if __name__ == "__main__":
    inisialisasi_data()
    while True:
        try:
            menu_utama()
            break
        except KeyboardInterrupt:
            print("\nNo No Yaa!")
        except EOFError:
            print("\nNo No Yaa!")

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

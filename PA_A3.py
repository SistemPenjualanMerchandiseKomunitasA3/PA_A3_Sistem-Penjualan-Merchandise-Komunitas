import os
import time
import json
from prettytable import PrettyTable
from pwinput import pwinput
import random

def bersih():   
    os.system("cls")

def asalpicik(pesan):
    while True:
        try:
            return input(pesan)
        except KeyboardInterrupt:
            print("\nNo No Yaa!\n")
        except EOFError:
            print("\nNo No Yaa!")
        
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

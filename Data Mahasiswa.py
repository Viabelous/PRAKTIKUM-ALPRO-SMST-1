#Ibnu Yafi Arya Wardana--2109106039--A21 Informatika

from os import system
from typing import Dict

def clear():
    _ = system('cls')

x = 0
Nama = "Belum ada data"
NIM = "Belum ada data"
Prodi = "Belum ada data"
Fakultas = "Belum ada data"
Tinggi = "Belum ada data"
Berat = "Belum ada data"

while x == 0:
    Statuses = {"Nama":Nama,"NIM":NIM,"Prodi":Prodi,"Fakultas":Fakultas,"Tinggi":Tinggi,"Berat":Berat}

    print("Data Mahasiswa:")
    if Nama == "Belum ada data":
        print("\t\033[0;31;40m[1] Nama Mahasiswa (Belum Diisi)\033[0;37;40m")
    else:
        print("\t\033[0;32;40m[1] Nama Mahasiswa\033[0;37;40m")
    if NIM == "Belum ada data":
        print("\t\033[0;31;40m[2] Nomor Induk Mahasiswa (Belum Diisi)\033[0;37;40m")
    else:
        print("\t\033[0;32;40m[2] Nomor Induk Mahasiswa\033[0;37;40m")
    if Prodi == "Belum ada data":
        print("\t\033[0;31;40m[3] Program Studi (Belum Diisi)\033[0;37;40m")
    else:
        print("\t\033[0;32;40m[3] Program Studi\033[0;37;40m")
    if Fakultas == "Belum ada data":
        print("\t\033[0;31;40m[4] Fakultas (Belum Diisi)\033[0;37;40m")
    else:
        print("\t\033[0;32;40m[4] Fakultas\033[0;37;40m")
    if Tinggi == "Belum ada data":
        print("\t\033[0;31;40m[5] Tinggi Badan (Belum Diisi)\033[0;37;40m")
    else:
        print("\t\033[0;32;40m[5] Tinggi\033[0;37;40m")
    if Berat == "Belum ada data":
        print("\t\033[0;31;40m[6] Berat Badan (Belum Diisi)\033[0;37;40m")
    else:
        print("\t\033[0;32;40m[6] Berat Badan\033[0;37;40m")
    print("\t\033[0;36;40m[7] Cek Data Mahasiswa\n\t[8] Keluar\033[0;37;40m")
    print('"tips: Cukup ketik angka di depan data yang hendak Anda edit"\n')

    MyChoice = str(input("Pilih: "))

    if MyChoice == "1" :
        Nama = str(input("Masukkan nama: "))
        print("[Data Tersimpan] Nama anda adalah:",Nama)
        input()
        clear()

    elif MyChoice == "2" :
        NIM = int(input("Masukkan NIM: "))
        print("[Data Tersimpan] Nomor Induk Mahasiswa Anda adalah:",NIM)
        input()
        clear()

    elif MyChoice == "3" :
        Prodi = str(input("Masukkan prodi: "))
        print("[Data Tersimpan] Program Studi Anda adalah:",Prodi)
        input()
        clear()

    elif MyChoice == "4" :
        Fakultas = str(input("Masukkan fakultas: "))
        print("[Data Tersimpan] Fakultas Anda adalah:",Fakultas)
        input()
        clear()

    elif MyChoice == "5" :
        Tinggi = float(input("Masukkan tinggi badan: "))
        print("[Data Tersimpan] Tinggi Badan Anda adalah:",Tinggi)
        input()
        clear()

    elif MyChoice == "6" :
        Berat = float(input("Masukkan berat badan: "))
        print("[Data Tersimpan] Berat Badan Anda adalah:",Berat)
        input()
        clear()

    elif MyChoice == "7" :
        for key, value in Statuses.items():
            print (key,':',value)
        input()
        clear()

    elif MyChoice == "8" :
        clear()
        print("\033[2;36;40m Terimakasih telah menggunakan layanan Kami!\033[0;37;40m")
        input()
        break

    else:
        print("==== Maaf, menu", MyChoice ,"tidak tersedia atau belum tersedia.. ====\n")
        input()
        clear()





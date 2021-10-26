#Nama: Ibnu Yafi Arya Wardana
#NIM: 2109106039
#Kelas: A'21 Informatika

from os import system

def clear():
    _ = system('cls')

x = 0
loof = 1

while loof == 1:
    if x==0:
        print("""Selamat Datang!""")
        x = 1
    else:
        print("Selamat Datang Kembali!")

    print("""Berikut converter yang kami sediakan:
    [1] Fahrenheit ke Celsius
    [2] Kelvin ke Celsius
    [3] Reamur ke Celsius
    [4] Suhu tanpa nama ke Celsius""")
    print('"tips: Cukup ketik angka di depan pilihan"\n')

    MyChoice = str(input("Pilihan Saya: "))

    if MyChoice == "1" :
        Suhu = float(input("Suhu Pada Termometer Saya adalah "))
        Suhu = (Suhu - 32) * 5 / 9
        print ("\tSuhu dalam Celcius: ",Suhu,"°C")

        while loof == 1:
            Pengulangan = input("\n\nUlangi (y/n)? ")
            if Pengulangan == "y":
                clear()
                break
            elif Pengulangan == "n":
                print("Terimakasih telah memakai layanan Kami~")
                loof += 1
                input()
                continue
            else:
                ErrorCom = input("Mohon ketik y atau n!")
                continue

    elif MyChoice == "2" :
        Suhu = float(input("Suhu Pada Termometer Saya adalah "))
        Suhu = (Suhu - 273)
        print ("\tSuhu dalam Celcius: ",Suhu,"°C")

        while loof == 1:
            Pengulangan = input("\n\nUlangi (y/n)? ")
            if Pengulangan == "y":
                clear()
                break
            elif Pengulangan == "n":
                print("Terimakasih telah memakai layanan Kami~")
                loof += 1
                input()
                continue
            else:
                ErrorCom = input("Mohon ketik y atau n!")
                continue

    elif MyChoice == "3" :
        Suhu = float(input("Suhu Pada Termometer Saya adalah "))
        Suhu = Suhu * 5 / 4
        print ("\tSuhu dalam Celcius: ",Suhu,"°C")

        while loof == 1:
            Pengulangan = input("\n\nUlangi (y/n)? ")
            if Pengulangan == "y":
                clear()
                break
            elif Pengulangan == "n":
                print("Terimakasih telah memakai layanan Kami~")
                loof += 1
                input()
                continue
            else:
                ErrorCom = input("Mohon ketik y atau n!")
                continue

    elif MyChoice == "4" :
        Suhu = float(input("Suhu Pada Termometer Saya adalah "))
        TDidih = float(input("Titik Didih Termometer Saya adalah "))
        TBeku = float(input("Titik Beku Termometer Saya adalah "))
        Suhu = (Suhu - TBeku) * 100 / (TDidih - TBeku)
        print ("\tSuhu dalam Celcius: ",Suhu,"°C")
         
        while loof == 1:
            Pengulangan = input("\n\nUlangi (y/n)? ")
            if Pengulangan == "y":
                clear()
                break
            elif Pengulangan == "n":
                print("Terimakasih telah memakai layanan Kami~")
                loof += 1
                input()
                continue
            else:
                ErrorCom = input("Mohon ketik y atau n!")
                continue

    else:
        print("==== Maaf, menu", MyChoice ,"tidak tersedia.. ====\n")
        input()
        clear()

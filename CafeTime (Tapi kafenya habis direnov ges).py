from os import system
import datetime

#2109106039

# for Admin Mode type  0-0  or  ViabelOnlyAccess  in Main Menu"
#
# Gate Key:
#   █▓ NorthGate: 1
#   █▓ MiddleGate: 4
#   █▓ SouthGate: 0
#   █▓ MainGate: 22

HargaTotal = 0
Diskon = 0
Intro = 0
MenuAwal = 0
Makanan = 0
Minuman = 0
Pesanan = {}
PesananCair = {}

MenuMakanan = [
["Strawberry Parfait", 10],
["Red Velvet Cake", 13],
["Dark Chocolate Cake", 14],
["Summery Fruit Salad", 8],
["Black Sesame Tart", 10],
["Chocolate Truffle", 4]
]

MenuMinuman = [
["Mineral Water", 1],
["Dalgona Coffee", 4],
["Mixed Fruits Juice", 2],
["Mixed Veggies Juice", 2],
["Thai Tea", 4],
["White Coffee", 3],
["Irish Coffe", 4],
["Caffé Latte", 3],
["Espresso Macchiato", 3],
["Lemon Squash", 3],
["O (Coffee)",2],
["Valencia Fizz", 3],
["Electrolyte Drinks", 7]
]

day = datetime.datetime.today().weekday()
if day <= 4:
    Diskon += 10
else:
    Diskon += 5

#IC = Ivory Coins, Mata uang negara entah negara mana ini

def Banner():
    print(100 * "*")
    print("\033[1;36;40mCafé Pour La Tâche\033[0;37;40m".center(100, " "))
    print(100 * "*")

def ViabelBanner():
    print("\033[1;32;40m")
    print(100 * "*")
    print("Café Pour La Tâche (Viabel Mode)".center(100, " "))
    print(100 * "*")

def clear():
    _ = system('cls')
_ = system('')

while MenuAwal == 0:
    if Intro == 0:
        print("\033[0;37;40m")
        print(100 * "*")
        print("\033[1;36;40mWelcome to our Café, Comrade!\033[0;37;40m".center(100, " "))
        print(100 * "*")

        print("\n\033[0;33;40m V: \"Saya, Viabel, akan membimbing Anda dalam melakukan pemesanan~\"\033[0;37;40m\n")
        Intro += 1
    else:
        clear()
        Banner()

    print(""" Berikut Opsi Jenis Menu yang dapat Anda pilih:
    [1] Menu Makanan
    [2] Menu Minuman
    [3] Menu Pembayaran""")
    print("\033[0;33;40m V: \"Ketik angka di depan menu, contoh: 1 (untuk makanan)\"\033[0;37;40m")
    Home = input(" Pilihan saya: ")
    if Home == "1":
        Food = 0
        while Food == 0:
            clear()
            Banner()
            print("Berikut Daftar Makanan beserta Harganya:")
            angka = 1
            for Menu, Harga in MenuMakanan:
                if len(Menu) < 12 :
                    print (f"\t\t[{angka}] {Menu}\t\t\t{Harga} IC")
                else:
                    print (f"\t\t[{angka}] {Menu}\t\t{Harga} IC")
                angka += 1
            print("\033[0;33;40m V: \"Pembelian 2 makanan atau lebih bisa dapat diskon 5% loh!\033[0;37;40m")
            print("\033[0;33;40m V: \"Ketik angka di depan menu, contoh: 1\"\033[0;37;40m")
            print("\033[0;33;40m V: \"Untuk mengubah pesanan, pilih kembali pesanan dan ketik jumlah yang diinginkan\"\033[0;37;40m")
            print("\033[0;33;40m V: \"Ketik \"Kembali\" atau \"0\" untuk kembali ke daftar menu utama\033[0;37;40m")

            FoodChoice = str(input(" Pilihan saya: "))

            if FoodChoice.casefold() == "kembali" or  FoodChoice == "0":
                break

            else:
                try:
                    AngkaDitunjuk = int(FoodChoice)
                    AngkaDitunjuk -= 1
                    if AngkaDitunjuk > angka - 2 or AngkaDitunjuk < 0:
                        print("\n\033[0;33;40m V: \"Hei.. Kami tidak memiliki menu rahasia seperti yang Anda pikirkan..\"\033[0;37;40m")
                        input()
                        clear()
                        continue
                    else:
                        if MenuMakanan[AngkaDitunjuk][0] in Pesanan:
                            HargaTotal -= MenuMakanan[AngkaDitunjuk][1] * Pesanan[MenuMakanan[AngkaDitunjuk][0]]
                            Makanan -= Pesanan[MenuMakanan[AngkaDitunjuk][0]]
                            Pesanan.pop(MenuMakanan[AngkaDitunjuk][0])
                        MyReq = int(input("\n Berapa banyak pesanan Anda? "))
                        try:
                            if MyReq >= int(1):
                                Pesanan[MenuMakanan[AngkaDitunjuk][0]] = MyReq
                                HargaTotal += MenuMakanan[AngkaDitunjuk][1] * MyReq
                                Makanan += MyReq
                                print(" Pesanan Ditambahkan!")
                                input()
                                clear()
                            elif MyReq >= int(0):
                                print(" Pesanan Dihapus")
                                input()
                                clear()
                            else:
                                print(" Jumlah pesanan tidak boleh kurang dari 0!")
                                input()
                                clear()
                        except ValueError:
                            print(" Jumlah Pesanan Tidak Valid")
                            input()
                            clear()
                except ValueError:
                    print("\n\033[0;33;40m V: \"Hei.. Kami tidak memiliki menu rahasia seperti yang Anda pikirkan..\"\033[0;37;40m")
                    input()
                    clear()
            

        

    elif Home == "2":
        Drink = 0
        while Drink == 0:
            clear()
            Banner()
            print("Berikut Daftar Minuman beserta Harganya:")
            angka = 1
            for Menu, Harga in MenuMinuman:
                if len(Menu) < 12 :
                    print (f"\t\t[{angka}] {Menu}\t\t\t{Harga} IC")
                else:
                    print (f"\t\t[{angka}] {Menu}\t\t{Harga} IC")
                angka += 1
            print("\033[0;33;40m V: \"Pembelian 3 minuman atau lebih bisa dapat diskon 10% loh!\033[0;37;40m")
            print("\033[0;33;40m V: \"Ketik angka di depan menu, contoh: 1\"\033[0;37;40m")
            print("\033[0;33;40m V: \"Untuk mengubah pesanan, pilih kembali pesanan dan ketik jumlah yang diinginkan\"\033[0;37;40m")
            print("\033[0;33;40m V: \"Ketik \"Kembali\" atau \"0\" untuk kembali ke daftar menu utama\033[0;37;40m")

            DrinkChoice = str(input(" Pilihan saya: "))
            if DrinkChoice.casefold() == "kembali" or  DrinkChoice == "0":
                break

            else:
                try:
                    AngkaDitunjuk = int(DrinkChoice)
                    AngkaDitunjuk -= 1
                    if AngkaDitunjuk > angka - 2 or AngkaDitunjuk < 0:
                        print("\n\033[0;33;40m V: \"Hei.. Kami tidak memiliki menu rahasia seperti yang Anda pikirkan..\"\033[0;37;40m")
                        input()
                        clear()
                        continue
                    else:
                        if MenuMinuman[AngkaDitunjuk][0] in PesananCair:
                            HargaTotal -= MenuMinuman[AngkaDitunjuk][1] * Pesanan[MenuMinuman[AngkaDitunjuk][0]]
                            Minuman -= PesananCair[MenuMinuman[AngkaDitunjuk][0]]
                            PesananCair.pop(MenuMinuman[AngkaDitunjuk][0])
                        MyReq = int(input("\n Berapa banyak pesanan Anda? "))
                        try:
                            if MyReq >= int(1):
                                PesananCair[MenuMinuman[AngkaDitunjuk][0]] = MyReq
                                HargaTotal += MenuMinuman[AngkaDitunjuk][1] * MyReq
                                Minuman += MyReq
                                print(" Pesanan Ditambahkan!")
                                input()
                                clear()
                            elif MyReq >= int(0):
                                print(" Pesanan Dihapus")
                                input()
                                clear()
                            else:
                                print(" Jumlah pesanan tidak boleh kurang dari 0!")
                                input()
                                clear()
                        except ValueError:
                            print(" Jumlah Pesanan Tidak Valid")
                            input()
                            clear()
                except ValueError:
                    print("\n\033[0;33;40m V: \"Hei.. Kami tidak memiliki menu rahasia seperti yang Anda pikirkan..\"\033[0;37;40m")
                    input()
                    clear()

    elif Home == "3":
        while MenuAwal == 0:
            clear()
            Banner()
            print(" Daftar Pesanan Anda: \n")
            for Menu, value in Pesanan.items():
                print (" ", Menu,'sebanyak',value, 'pcs')
            for Menu, value in PesananCair.items():
                print (" ", Menu,'sebanyak',value, 'gelas')
            GrandFinale = str(input("\n Lanjut ke proses pembayaran (yes/no)? "))
            if GrandFinale.casefold() == "yes" or GrandFinale.casefold() == "ya" or GrandFinale.casefold() == "y":
                Emoney = str(input("\n Apa anda ingin membayar dengan e-money(yes/no)? "))
                if Emoney.casefold() == "yes" or Emoney.casefold() == "ya" or Emoney.casefold() == "y":
                    Diskon += 5
                    print()
                elif Emoney.casefold() == "no" or Emoney.casefold() == "tidak" or Emoney.casefold() == "n":
                    print()
                else:
                    print(" Menu pembayaran",Emoney,"tidak ada, jawaban otomatis: tidak")
                    input()
                clear()
                Banner()
                print("\n\n")
                print("|" * 50)
                print(" Setelah menambahkan diskon: \n")

                if Makanan >= 2:
                    print(" Diskon pembelian minimal 2 makanan sebesar 5%")
                    Diskon += 5
                if Minuman >= 3:
                    print(" Diskon pembelian minimal 3 minuman sebesar 10%")
                    Diskon += 10
                if Emoney == "yes":
                    print(" Diskon penggunaan E-money sebesar 5%")
                if day >= 5:
                    print(" Diskon weekend sebesar 5%")
                else:
                    print(" Diskon weekdays sebesar 10%")
                print("|" * 50)

                HargaTotal = int(HargaTotal - HargaTotal * Diskon / 100)
                print("\n\n \033[1;37;41m Harga yang harus Anda bayar: ", HargaTotal, "Ivory Coins\033[1;37;40m")
                input()
                quit()

            elif GrandFinale.casefold() == "no" or GrandFinale.casefold() == "tidak" or GrandFinale.casefold() == "n":
                clear()
                break
            else:
                print("\n\033[0;33;40m V: \"Mohon ketik \"yes\" atau \"no\"\"\033[0;37;40m")
                input()
    
    elif Home == "ViabelOnlyAccess" or Home == "0-0":
        clear()
        Banner()
        print("\033[1;32;40m AI: \"HI, Viabel, Please Double Check\"")
        Gate1 = input(" █▓▒ NorthGate:\t\t")
        Gate2 = input(" █▓▒ MiddleGate:\t")
        Gate3 = input(" █▓▒ SouthGate:\t\t")
        Locks = input(" █▓▒ MainGate:\t\t")
        if Gate1 == "1" and Gate2 == "4" and Gate3 == "0" and Locks == "22":
            while MenuAwal == 0:
                clear()
                ViabelBanner()
                print(" AI: \"It\'s Viabel!!\"")
                print(""" Berikut Opsi Jenis Menu yang dapat diubah:
    [1] Menu Makanan
    [2] Menu Minuman
    [3] Keluar""")
                print(" AI: \"Ketik angka di depan menu, contoh: 1 (untuk makanan)")
                HomeOfSecrets = input(" Pilihan Viabel: ")
                if HomeOfSecrets == "1":
                    Food = 0
                    while Food == 0:
                        clear()
                        ViabelBanner()
                        print("Berikut Daftar Makanan beserta Harganya:")
                        angka = 1
                        for Menu, Harga in MenuMakanan:
                            if len(Menu) < 12 :
                                print (f"\t\t[{angka}] {Menu}\t\t\t{Harga} IC")
                            else:
                                print (f"\t\t[{angka}] {Menu}\t\t{Harga} IC")
                            angka += 1
                        print(' AI: "Pembelian 2 makanan mendapat diskon 5%"')
                        print(' AI: "Ketik angka di depan menu yang ingin diubah, contoh: 1"')
                        print(' AI: "Untuk menambah menu makanan, ketik "add" atau "002""')
                        print(' AI: "Ketik "Kembali" atau "0" untuk kembali ke daftar menu utama"')
                        print(' AI: "Reset Semua Menu? Ketik: NuclearDelete"')

                        FoodChoice = str(input(" Pilihan Viabel: "))
                        if FoodChoice == "NuclearDelete":
                            MenuMakanan.clear()
                            print(' AI: Berhasil Dihapus!')
                        elif FoodChoice.casefold() == "kembali" or FoodChoice == "0":
                            clear()
                            break
                        elif FoodChoice.casefold() == "add" or FoodChoice == "002":
                            try:
                                NewMenu = str(input("\n Nama Menu Baru: "))
                                Price = int(input(" Harga untuk Menu Baru: "))
                                print('\n AI: "Ketik angka pemempatan di menu, misal: 1"')
                                print(' AI: "Untuk menambahkan menu di angka terakhir, ketik angka berapa saja"')
                                print(' AI: "\t\t\t\t\t\t(Selain angka di menu)"')
                                MenuPlacement = int(input(" Ketik angka penempatan di menu: "))
                                if MenuPlacement <= 0:
                                    print(' AI: "Yang benar saja.."')
                                    input()
                                    clear()
                                else:
                                    adding = [NewMenu, Price]
                                    MenuMakanan.insert(MenuPlacement - 1, adding)
                                    print(" Menu Berhasil Ditambahkan!")
                            except ValueError:
                                NewMenu = ()
                                MenuPlacement = ()
                                print(' AI: "Yang benar saja.."')
                                input()
                                clear()
                        else:
                            try: 
                                AngkaDitunjuk = int(FoodChoice)
                                AngkaDitunjuk -= 1
                                if AngkaDitunjuk > angka - 2 or AngkaDitunjuk < 0:
                                    print(' AI: "Yang benar saja.."')
                                    input()
                                    clear()
                                    continue
                                else:
                                    print(" [1] Ubah Nama Menu\t[2] Ubah Harga\t[3] Hapus Menu\t[4] Batalkan ")
                                    Edit = str(input(" Opsi: "))
                                    if Edit == "1":
                                        NamaBaru = str(input(" Masukkan Nama Baru: "))
                                        MenuMakanan[AngkaDitunjuk][0] = NamaBaru
                                        print(" Nama berhasil diperbarui!")
                                        input()
                                        clear()
                                    elif Edit == "2":
                                            HargaBaru = int(input(" Masukkan Harga Baru: "))
                                            MenuMakanan[AngkaDitunjuk][1] = HargaBaru
                                            print(" Harga berhasil diperbarui!")
                                            input()
                                            clear()
                                    elif Edit == "3":
                                            del MenuMakanan[AngkaDitunjuk]
                                            print(" Menu Berhasil Dihapus!")
                                            input()
                                            clear()
                                    elif Edit == "4":
                                        clear()
                                    else:
                                        print(' AI: "Yang benar saja.."')
                                        input()
                                        clear()

                            except ValueError:
                                print(' AI: "Yang benar saja.."')
                                input()
                                clear()
                elif HomeOfSecrets == "2":
                    Drink = 0
                    while Drink == 0:
                        clear()
                        ViabelBanner()
                        print("Berikut Daftar Makanan beserta Harganya:")
                        angka = 1
                        for Menu, Harga in MenuMinuman:
                            if len(Menu) < 12 :
                                print (f"\t\t[{angka}] {Menu}\t\t\t{Harga} IC")
                            else:
                                print (f"\t\t[{angka}] {Menu}\t\t{Harga} IC")
                            angka += 1
                        print(' AI: "Pembelian 3 minuman mendapat diskon 10%"')
                        print(' AI: "Ketik angka di depan menu yang ingin diubah, contoh: 1"')
                        print(' AI: "Untuk menambah menu minuman, ketik "add" atau "002""')
                        print(' AI: "Ketik "Kembali" atau "0" untuk kembali ke daftar menu utama"')
                        print(' AI: "Reset Semua Menu? Ketik: NuclearDelete"')

                        DrinkChoice = str(input(" Pilihan Viabel: "))
                        if DrinkChoice == "NuclearDelete":
                            MenuMinuman.clear()
                            print(' AI: Berhasil Dihapus!')
                        elif DrinkChoice.casefold() == "kembali" or DrinkChoice == "0":
                            clear()
                            break
                        elif DrinkChoice.casefold() == "add" or DrinkChoice == "002":
                            try:
                                NewMenu = str(input("\n Nama Menu Baru: "))
                                Price = int(input(" Harga untuk Menu Baru: "))
                                print('\n AI: "Ketik angka pemempatan di menu, misal: 1"')
                                print(' AI: "Untuk menambahkan menu di angka terakhir, ketik angka berapa saja"')
                                print(' AI: "\t\t\t\t\t\t(Selain angka di menu)"')
                                MenuPlacement = int(input(" Ketik angka penempatan di menu: "))
                                if MenuPlacement <= 0:
                                    print(' AI: "Yang benar saja.."')
                                    input()
                                    clear()
                                else:
                                    adding = [NewMenu, Price]
                                    MenuMakanan.insert(MenuPlacement - 1, adding)
                                    print(" Menu Berhasil Ditambahkan!")
                            except ValueError:
                                NewMenu = ()
                                MenuPlacement = ()
                                print(' AI: "Yang benar saja.."')
                                input()
                                clear()
                        else:
                            try: 
                                AngkaDitunjuk = int(DrinkChoice)
                                AngkaDitunjuk -= 1
                                if AngkaDitunjuk > angka - 2 or AngkaDitunjuk < 0:
                                    print(' AI: "Yang benar saja.."')
                                    input()
                                    clear()
                                    continue
                                else:
                                    print(" [1] Ubah Nama Menu\t[2] Ubah Harga\t[3] Hapus Menu\t[4] Batalkan ")
                                    Edit = str(input(" Opsi: "))
                                    if Edit == "1":
                                        NamaBaru = str(input(" Masukkan Nama Baru: "))
                                        MenuMinuman[AngkaDitunjuk][0] = NamaBaru
                                        print(" Nama berhasil diperbarui!")
                                        input()
                                        clear()
                                    elif Edit == "2":
                                            HargaBaru = int(input(" Masukkan Harga Baru: "))
                                            MenuMinuman[AngkaDitunjuk][1] = HargaBaru
                                            print(" Harga berhasil diperbarui!")
                                            input()
                                            clear()
                                    elif Edit == "3":
                                            del MenuMinuman[AngkaDitunjuk]
                                            print(" Menu Berhasil Dihapus!")
                                            input()
                                            clear()
                                    elif Edit == "4":
                                        clear()
                                    else:
                                        print(' AI: "Yang benar saja.."')
                                        input()
                                        clear()

                            except ValueError:
                                print(' AI: "Yang benar saja.."')
                                input()
                                clear()
                elif HomeOfSecrets == "3":
                    break
                else:
                    print(' AI: "Yang benar saja.."')
                    input()

        else:
            clear()
            print("\033[1;31;40m V: \"You shouldn't be here..\"\n" * 1000)
            input()
            quit()
    else:        
        print("\n\033[0;33;40m V: \"Menunya gaada.. (atau belum ada?)\"\033[0;37;40m")
        input()

from os import system
import datetime

# 2109106039

# IC = Ivory Coins, Mata uang negara entah negara mana ini
# for Admin Mode type  0-0  or  ViabelOnlyAccess  in Main Menu"
#
# Gate Key:
#   █▓ NorthGate: 1
#   █▓ MiddleGate: 4
#   █▓ SouthGate: 0
#   █▓ MainGate: 22




# Deklarasi # Deklarasi # Deklarasi # Deklarasi # Deklarasi # Deklarasi
HargaTotal = 0
Diskon = 0
Intro = 0
Makanan = 0
Minuman = 0
Pesanan = {}
PesananCair = {}
Emoney = "no"
Gate = ["North","Middle","South","Main"]

MenuMakanan = {
"Sp" : {"Strawberry Parfait" : 10},
"Rvc" : {"Red Velvet Cake": 13},
"Dcc" : {"Dark Chocolate Cake" : 14},
"Smf" : {"Summery Fruit Salad" : 8},
"Bst" : {"Black Sesame Tart" : 10},
"Ct" : {"Chocolate Truffle" : 4},
"Lm" : {"Love Muffin" : 8},
"Cn" : {"Chicken Nuggets" : 4}
}

MenuMinuman = {
"Mw" : {"Mineral Water" : 1},
"Dc" : {"Dalgona Coffee" : 4},
"Fj" : {"Fruits Juice" : 2},
"Vj" : {"Veggies Juice" : 2},
"Tt" : {"Thai Tea" : 4},
"Wc" : {"White Coffee" : 3},
"Ic" : {"Irish Coffe" : 4},
"Cl" : {"Caffé Latte" : 3},
"Em" : {"Espresso Macchiato" : 3},
"Ls" : {"Lemon Squash" : 3},
"O" : {"O (Coffee)" : 2},
"Vf" : {"Valencia Fizz" : 3},
"Ed" : {"Electrolyte Drinks" : 7}
}




# Diskon # Diskon # Diskon # Diskon # Diskon # Diskon
def DiskonHari(Diskon, Day):
    if Day <= 4:
        Diskon += 10
        return Diskon
    else:
        Diskon += 5
        return Diskon

def Diskons(Makanan, Minuman, Emoney, Diskon):
    Day = datetime.datetime.today().weekday()
    if Makanan >= 2:
        print(" Diskon pembelian minimal 2 makanan sebesar 5%")
        Diskon += 5
    if Minuman >= 3:
        print(" Diskon pembelian minimal 3 minuman sebesar 10%")
        Diskon += 10
    if Emoney.casefold() == "yes" or Emoney.casefold() == "ya" or Emoney.casefold() == "y":
        print(" Diskon penggunaan E-money sebesar 5%")
        Diskon += 5
    if Day >= 5:
        print(" Diskon weekend sebesar 5%")
        Diskon = DiskonHari(Diskon, Day)
    else:
        print(" Diskon weekdays sebesar 10%")
        Diskon = DiskonHari(Diskon, Day)
    return Diskon




# Dekorasi # Dekorasi # Dekorasi # Dekorasi # Dekorasi # Dekorasi 
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




# Main Menu # Main Menu # Main Menu # Main Menu # Main Menu # Main Menu
def FirstTimeMainMenu(Intro):
    print("\033[0;37;40m")
    print(100 * "*")
    print("\033[1;36;40mWelcome to our Café, Comrade!\033[0;37;40m".center(100, " "))
    print(100 * "*")

    print("\n\033[0;33;40m V: \"Saya, Viabel, akan membimbing Anda dalam melakukan pemesanan~\"\033[0;37;40m\n")
    Intro += 1
    return Intro

def MainMenu():
    print(""" Berikut Opsi Jenis Menu yang dapat Anda pilih:
        [1] Menu Makanan
        [2] Menu Minuman
        [3] Menu Pembayaran""")
    print("\033[0;33;40m V: \"Ketik angka di depan menu, contoh: 1 (untuk makanan)\"\033[0;37;40m")
    Home = input(" Pilihan saya: ")
    return Home

def NormalMenu(Intro, Home):
    if Intro == 0:
        Intro = FirstTimeMainMenu(Intro)
        Home = MainMenu()
    else:
        clear()
        Banner()
        Home = MainMenu()
    return Intro, Home

def ViabelMainMenu():
    print(" AI: \"It\'s Viabel!!\"")
    print(""" Berikut Opsi Jenis Menu yang dapat diubah:
    [1] Menu Makanan
    [2] Menu Minuman
    [3] Keluar""")
    print(" AI: \"Ketik angka di depan menu, contoh: 1 (untuk makanan)")
    HomeOfSecrets = input(" Pilihan Viabel: ")
    return HomeOfSecrets




# Food Menu # Food Menu # Food Menu # Food Menu # Food Menu # Food Menu
def FoodPhase(HargaTotal, Makanan):
    while True:
        clear()
        Banner()
        KodeDitunjuk = FoodMenu("Thru")
        if KodeDitunjuk.casefold() == "kembali" or  KodeDitunjuk == "0":
            break
        else:
            try:
                if KodeDitunjuk not in MenuMakanan:
                    UsualError()
                else:
                    Feed = MenuMakanan[KodeDitunjuk]
                    for Key in Feed:
                        NamaMakanan = Key
                        HargaMakanan = Feed.get(Key)

                    if NamaMakanan in Pesanan:
                        HargaTotal, Makanan = MakananPernahDipesan(HargaTotal, Makanan, NamaMakanan, HargaMakanan)

                    HargaTotal, Makanan = MakananDipesan(HargaTotal, Makanan, NamaMakanan, HargaMakanan)
            except ValueError:
                UsualError()
    return HargaTotal, Makanan

def FoodMenu(Pathway):
    print("Berikut Daftar Makanan beserta Harganya:")
    for MenuNum, Menu in MenuMakanan.items():
        for NamaMenu in Menu:
            if len(NamaMenu) < 11 :
                print (f"\t\t[{MenuNum}] {NamaMenu}\t\t\t{Menu[NamaMenu]} IC")
            elif len(NamaMenu) < 19:
                print (f"\t\t[{MenuNum}] {NamaMenu}\t\t{Menu[NamaMenu]} IC")
            else :
                print (f"\t\t[{MenuNum}] {NamaMenu}\t{Menu[NamaMenu]} IC")
    if Pathway == "Thru":
        FoodMenuNotice()
    else:
        ViabelFoodMenuNotice()

    KodeDitunjuk = str(input(" Pilihan saya: "))
    return KodeDitunjuk

def MakananPernahDipesan(HargaTotal, Makanan, HargaMakanan, NamaMakanan):
    HargaTotal -= HargaMakanan * Pesanan[NamaMakanan]
    Makanan -= Pesanan[NamaMakanan]
    Pesanan.pop(NamaMakanan)
    return HargaTotal, Makanan

def MakananDipesan(HargaTotal, Makanan, NamaMakanan, HargaMakanan):
    MyReq = int(input("\n Berapa banyak pesanan Anda? "))
    try:
        if MyReq >= int(1):
            Pesanan[NamaMakanan] = MyReq
            HargaTotal += HargaMakanan * MyReq
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
    return HargaTotal, Makanan




# Drink Menu # Drink Menu # Drink Menu # Drink Menu # Drink Menu # Drink Menu
def DrinkPhase(HargaTotal, Minuman):
    while True:
        clear()
        Banner()
        KodeDitunjuk = DrinkMenu("Thru")
        if KodeDitunjuk.casefold() == "kembali" or  KodeDitunjuk == "0":
            break
        else:
            try:
                if KodeDitunjuk not in MenuMinuman:
                    UsualError()
                else:
                    Feed = MenuMinuman[KodeDitunjuk]
                    for Key in Feed:
                        NamaMinuman = Key
                        HargaMinuman = Feed.get(Key)

                    if NamaMinuman in PesananCair:
                        HargaTotal, Minuman = MinumanPernahDipesan(HargaTotal, Minuman, NamaMinuman, HargaMinuman)

                    HargaTotal, Minuman = MinumanDipesan(HargaTotal, Minuman, NamaMinuman, HargaMinuman)
            except ValueError:
                UsualError()
    return HargaTotal, Minuman

def DrinkMenu(Pathway):
    print("Berikut Daftar Minuman beserta Harganya:")
    angka = 0
    for MenuNum, Menu in MenuMinuman.items():
        for NamaMenu in Menu:
            angka += 1
            if len(NamaMenu) < 11 :
                print (f"\t\t[{MenuNum}] {NamaMenu}\t\t\t{Menu[NamaMenu]} IC")
            elif len(NamaMenu) < 19:
                print (f"\t\t[{MenuNum}] {NamaMenu}\t\t{Menu[NamaMenu]} IC")
            else:
                print (f"\t\t[{MenuNum}] {NamaMenu}\t{Menu[NamaMenu]} IC")
    if Pathway == "Thru":
        DrinkMenuNotice()
    else:
        ViabelDrinkMenuNotice()

    KodeDitunjuk = str(input(" Pilihan saya: "))
    return KodeDitunjuk

def MinumanPernahDipesan(HargaTotal, Minuman, HargaMinuman, NamaMinuman):
    HargaTotal -= HargaMinuman * Pesanan[NamaMinuman]
    Minuman -= Pesanan[NamaMinuman]
    PesananCair.pop(NamaMinuman)
    return HargaTotal, Minuman

def MinumanDipesan(HargaTotal, Minuman, NamaMinuman, HargaMinuman):
    MyReq = int(input("\n Berapa banyak pesanan Anda? "))
    try:
        if MyReq >= int(1):
            PesananCair[NamaMinuman] = MyReq
            HargaTotal += HargaMinuman * MyReq
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
    return HargaTotal, Minuman




# Mass Notice
def FoodMenuNotice():
    print("\033[0;33;40m V: \"Pembelian 2 makanan atau lebih bisa dapat diskon 5% loh!\033[0;37;40m")
    print("\033[0;33;40m V: \"Ketik kode di depan menu, contoh: Sp\"\033[0;37;40m")
    print("\033[0;33;40m V: \"Untuk mengubah pesanan, pilih kembali pesanan dan ketik jumlah yang diinginkan\"\033[0;37;40m")
    print("\033[0;33;40m V: \"Ketik \"Kembali\" atau \"0\" untuk kembali ke daftar menu utama\033[0;37;40m")

def DrinkMenuNotice():
    print("\033[0;33;40m V: \"Pembelian 3 minuman atau lebih bisa dapat diskon 10% loh!\033[0;37;40m")
    print("\033[0;33;40m V: \"Ketik angka di depan menu, contoh: 1\"\033[0;37;40m")
    print("\033[0;33;40m V: \"Untuk mengubah pesanan, pilih kembali pesanan dan ketik jumlah yang diinginkan\"\033[0;37;40m")
    print("\033[0;33;40m V: \"Ketik \"Kembali\" atau \"0\" untuk kembali ke daftar menu utama\033[0;37;40m")

def ViabelFoodMenuNotice():
    print(' AI: "Pembelian 2 makanan mendapat diskon 5%"')
    print(' AI: "Ketik kode di depan menu yang ingin diubah, contoh: Sp"')
    print(' AI: "Untuk menambah menu makanan, ketik "add" atau "002""')
    print(' AI: "Ketik "Kembali" atau "0" untuk kembali ke daftar menu utama"')
    print(' AI: "Hapus Semua Menu? Ketik: NuclearDelete"')

def ViabelDrinkMenuNotice():
    print(' AI: "Pembelian 3 minuman mendapat diskon 10%"')
    print(' AI: "Ketik angka di depan menu yang ingin diubah, contoh: 1"')
    print(' AI: "Untuk menambah menu minuman, ketik "add" atau "002""')
    print(' AI: "Ketik "Kembali" atau "0" untuk kembali ke daftar menu utama"')
    print(' AI: "Reset Semua Menu? Ketik: NuclearDelete"')


# Pembayaran # Pembayaran # Pembayaran # Pembayaran # Pembayaran # Pembayaran 
def Pembayaran(HargaTotal, Diskon):
    while True:
        clear()
        Banner()
        DaftarPesanan()
        GrandFinale = str(input("\n Lanjut ke proses pembayaran (yes/no)? "))
        if GrandFinale.casefold() == "yes" or GrandFinale.casefold() == "ya" or GrandFinale.casefold() == "y":
            EmoneyOption()
            clear()
            Banner()
            print("\n\n")
            print("|" * 50)
            print(" Setelah menambahkan diskon: \n")
            Diskon = Diskons(Makanan, Minuman, Emoney, 0)
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

def DaftarPesanan():
    print(" Daftar Pesanan Anda: \n")
    for Menu, value in Pesanan.items():
        print (" ", Menu,'sebanyak',value, 'pcs')
    for Menu, value in PesananCair.items():
        print (" ", Menu,'sebanyak',value, 'gelas')

def EmoneyOption():
    Emoney = str(input("\n Apa anda ingin membayar dengan e-money(yes/no)? "))
    if Emoney.casefold() == "yes" or Emoney.casefold() == "ya" or Emoney.casefold() == "y":
        print()
    elif Emoney.casefold() == "no" or Emoney.casefold() == "tidak" or Emoney.casefold() == "n":
        print()
    else:
        print(" Menu pembayaran",Emoney,"tidak ada, jawaban otomatis: tidak")
        input()




# Secured by Gate
def ViabelGateway():
    print("\033[1;32;40m AI: \"HI, Viabel, Please Double Check\"")
    Gate[0] = input(" █▓▒ NorthGate:\t\t")
    Gate[1] = input(" █▓▒ MiddleGate:\t")
    Gate[2] = input(" █▓▒ SouthGate:\t\t")
    Gate[3] = input(" █▓▒ MainGate:\t\t")

def GateOpen():
    while True:
        clear()
        ViabelBanner()
        HomeOfSecrets = ViabelMainMenu()
        if HomeOfSecrets == "1":
            ViabelMenuPhase(MenuMakanan, FoodMenu)
        elif HomeOfSecrets == "2":
            ViabelMenuPhase(MenuMinuman, DrinkMenu)
        elif HomeOfSecrets == "3":
            break
        else:
            ProfessionalError()




# Menu Editor
def AddMenu(Menu):
    try:
        NewMenu = str(input("\n Nama Menu Baru: "))
        Price = int(input(" Harga untuk Menu Baru: "))
        Code = str(input(" Ketik kode untuk menu: "))
        if len(Code) <= 0:
            ProfessionalError()
        else:
            Menu[Code] = {NewMenu : Price} 
            print(" Menu Berhasil Ditambahkan!")
    except ValueError:
        NewMenu = ()
        Price = ()
        Code = ()
        ProfessionalError()

def EditMenu(KodeDitunjuk, Menu):
    try: 
        if KodeDitunjuk not in Menu:
            ProfessionalError()
        else:
            Feed = Menu[KodeDitunjuk]
            for Key in Feed:
                NamaLama = Key
                HargaLama = Feed.get(Key)
            print(" [1] Ubah Nama Menu\t[2] Ubah Harga\t[3] Ubah Kode\t[4] Hapus Menu\t [5] Batalkan ")
            Edit = str(input(" Opsi: "))

            if Edit == "1":
                NamaBaru = str(input(" Masukkan Nama Baru: "))
                Menu[KodeDitunjuk] = {NamaBaru : HargaLama}
                print(" Nama berhasil diperbarui!")
                input()
                clear()
            elif Edit == "2":
                HargaBaru = int(input(" Masukkan Harga Baru: "))
                Menu[KodeDitunjuk] = {NamaLama : HargaBaru}
                print(" Harga berhasil diperbarui!")
                input()
                clear()
            elif Edit == "3":
                KodeBaru = str(input(" Masukkan Kode Baru: "))
                Menu[KodeBaru] = MenuMakanan.pop(KodeDitunjuk)
                print(" Kode berhasil diperbarui!")
                input()
                clear()
            elif Edit == "4":
                del Menu[KodeDitunjuk]
                print(" Menu Berhasil Dihapus!")
                input()
                clear()
            elif Edit == "5":
                clear()
            else:
                ProfessionalError()
    except ValueError:
        ProfessionalError()

def ViabelMenuPhase(Menu, WhichMenu):
    while True:
        clear()
        ViabelBanner()
        KodeDitunjuk = WhichMenu(0)

        if KodeDitunjuk == "NuclearDelete":
            Menu.clear()
            print(' AI: Berhasil Dihapus!')
        elif KodeDitunjuk.casefold() == "kembali" or KodeDitunjuk == "0":
            clear()
            break
        elif KodeDitunjuk.casefold() == "add" or KodeDitunjuk == "002":
            AddMenu(Menu)
        else:
            EditMenu(KodeDitunjuk, Menu)



# Error # Error # Error # Error # Error # Error
def UsualError():
    print("\n\033[0;33;40m V: \"Hei.. Kami tidak memiliki menu rahasia seperti yang Anda pikirkan..\"\033[0;37;40m")
    input()
    clear()

def ProfessionalError():
    print(' AI: "Yang benar saja.."')
    input()
    clear()




# Program # Program # Program # Program # Program # Program
while True:
    Intro, Home = NormalMenu(Intro, 0)
    if Home == "1":
        HargaTotal, Makanan = FoodPhase(HargaTotal, Makanan)
            
    elif Home == "2":
        HargaTotal, Minuman = DrinkPhase(HargaTotal, Minuman)

    elif Home == "3":
        Pembayaran(HargaTotal, Diskon)
    
    elif Home == "ViabelOnlyAccess" or Home == "0-0":
        clear()
        Banner()
        ViabelGateway()
        
        if Gate[0] == "1" and Gate[1] == "4" and Gate[2] == "0" and Gate[3] == "22":
            GateOpen()

        else:
            clear()
            print("\033[1;31;40m V: \"You shouldn't be here..\"\n" * 1000)
            input()
            quit()
    else:        
        print("\n\033[0;33;40m V: \"Menunya gaada.. (atau belum ada?)\"\033[0;37;40m")
        input()

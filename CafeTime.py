from os import system
import datetime

#2109106039

HargaTotal = 0
Diskon = 0
Intro = 0
MenuAwal = 0
Makanan = 0
Minuman = 0
Pesanan = {}
PesananCair = {}

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

def clear():
    _ = system('cls')
_ = system('')
    

while MenuAwal == 0:
    if Intro == 0:
        print(100 * "*")
        print("\033[1;36;40mWelcome to our Café, Comrade!\033[0;37;40m".center(100, " "))
        print(100 * "*")

        print("\n\033[0;33;40m V: \"Saya, Viabel, akan membimbing Anda dalam melakukan pemesanan~\"\033[0;37;40m\n")
        Intro += 1
    else:
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
            print(""" Berikut Daftar Makanan beserta Harganya:
        [1] Strawberry Parfait\t [10 IC]\t <-- Recommendation
        [2] Red Velvet Cake\t [13 IC]
        [3] Dark Chocolate Cake\t [14 IC]
        [4] Summery Fruit Salad\t [ 8 IC]
        [5] Black Sesame Tart\t [10 IC]
        [6] Chocolate Truffle\t [ 4 IC]
            """)
            print("\033[0;33;40m V: \"Pembelian 2 makanan atau lebih bisa dapat diskon 5% loh!\033[0;37;40m")
            print("\033[0;33;40m V: \"Ketik angka di depan menu, contoh: 1 (untuk parfait)\"\033[0;37;40m")
            print("\033[0;33;40m V: \"Untuk mengubah pesanan, pilih kembali pesanan dan ketik jumlah yang diinginkan\"\033[0;37;40m")
            print("\033[0;33;40m V: \"Ketik \"Kembali\" atau \"0\" untuk kembali ke daftar menu utama\033[0;37;40m")

            FoodChoice = str(input(" Pilihan saya: "))

            if FoodChoice == "1":
                if 'Strawberry Parfait' in Pesanan:
                    HargaTotal -= 10 * SParf
                    Makanan -= SParf
                    Pesanan.pop('Strawberry Parfait') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                SParf = int(input(" Berapa banyak pesanan Anda? "))
                if SParf >= 1:
                    Pesanan['Strawberry Parfait'] = SParf
                    HargaTotal += 10 * SParf
                    Makanan += SParf
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif FoodChoice == "2":
                if 'Red Velvet Cake' in Pesanan:
                    HargaTotal -= 13 * RVCake
                    Makanan -= RVCake
                    Pesanan.pop('Red Velvet Cake') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                RVCake = int(input(" Berapa banyak pesanan Anda? "))
                if RVCake >= 1:
                    Pesanan['Red Velvet Cake'] = RVCake
                    HargaTotal += 13 * RVCake
                    Makanan += RVCake
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif FoodChoice == "3":
                if 'Dark Chocolate Cake' in Pesanan:
                    HargaTotal -= 14 * DCCake
                    Makanan -= DCCake
                    Pesanan.pop('Dark Chocolate') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                DCCake = int(input(" Berapa banyak pesanan Anda? "))
                if DCCake >= 1:
                    Pesanan['Dark Chocolate Cake'] = DCCake
                    HargaTotal += 14 * DCCake
                    Makanan += DCCake
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif FoodChoice == "4":
                if 'Summery Fruit Salad' in Pesanan:
                    HargaTotal -= 8 * SFSalad
                    Makanan -= SFSalad
                    Pesanan.pop('Summery Fruit Salad') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                SFSalad = int(input(" Berapa banyak pesanan Anda? "))
                if SFSalad >= 1 :
                    Pesanan['Summery Fruit Salad'] = SFSalad
                    HargaTotal += 8 * SFSalad
                    Makanan += SFSalad
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif FoodChoice == "5":
                if 'Black Sesame Tart' in Pesanan:
                    HargaTotal -= 10 * BSTart
                    Makanan -= BSTart
                    Pesanan.pop('Black Sesame Tart') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                BSTart = int(input(" Berapa banyak pesanan Anda? "))
                if BSTart >= 1:
                    Pesanan['Black Sesame Tart'] = BSTart
                    HargaTotal += 10 * BSTart
                    Makanan += BSTart
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif FoodChoice == "6":
                if 'Chocolate Truffle' in Pesanan:
                    HargaTotal -= 4 * CTruff
                    Makanan -= CTruff
                    Pesanan.pop('Chocolate Truffle') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                CTruff = int(input(" Berapa banyak pesanan Anda? "))
                if CTruff >= 1:
                    Pesanan['Chocolate Truffle'] = CTruff
                    HargaTotal += 4 * CTruff
                    Makanan += CTruff
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif FoodChoice.casefold() == "kembali" or  FoodChoice == "0":
                clear()
                break

            else:
                print("\n\033[0;33;40m V: \"Hei.. Kami tidak memiliki menu rahasia seperti yang Anda pikirkan..\"\033[0;37;40m")
                input()
                clear()
            

        

    elif Home == "2":
        Drink = 0
        while Drink == 0:
            clear()
            Banner()
            print(""" Berikut Daftar Minuman beserta Harganya:
        [1] Mineral Water\t [1 IC]
        [2] Dalgona Coffee\t [4 IC]
        [3] Mixed Fruits Juice\t [2 IC]
        [4] Mixed Veggies Juice\t [2 IC]
        [5] Thai Tea \t\t [4 IC]
        [6] White Coffee\t [3 IC]  <-- Recommendation
        [7] Irish Coffe\t\t [4 IC]  <-- Recommendation
        [8] Caffé Latte\t\t [3 IC]
        [9] Espresso Macchiato\t [3 IC]
        [10] Lemon Squash\t [3 IC] 
        [11] O (Coffee)\t\t [2 IC]
        [12] Valencia Fizz\t [3 IC]
        [13] Electrolyte Drinks\t [7 IC]
            """)
            print("\033[0;33;40m V: \"Pembelian 3 minuman atau lebih bisa dapat diskon 10% loh!\033[0;37;40m")
            print("\033[0;33;40m V: \"Ketik angka di depan menu, contoh: 1 (untuk Mineral Water)\"\033[0;37;40m")
            print("\033[0;33;40m V: \"Untuk mengubah pesanan, pilih kembali pesanan dan ketik jumlah yang diinginkan\"\033[0;37;40m")
            print("\033[0;33;40m V: \"Ketik \"Kembali\" atau \"0\" untuk kembali ke daftar menu utama\033[0;37;40m")

            DrinkChoice = str(input(" Pilihan saya: "))

            if DrinkChoice == "1":
                if 'Mineral Water' in PesananCair:
                    HargaTotal -= 1 * MWat
                    Minuman -= MWat
                    PesananCair.pop('Mineral Water') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                MWat = int(input(" Berapa banyak pesanan Anda? "))
                if MWat >= 1:
                    PesananCair['Mineral Water'] = MWat
                    HargaTotal += 1 * MWat
                    Minuman += MWat
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif DrinkChoice == "2":
                if 'Dalgona Coffee' in PesananCair:
                    HargaTotal -= 4 * DCof 
                    Minuman -= DCof
                    PesananCair.pop('Dalgona Coffee') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                DCof = int(input(" Berapa banyak pesanan Anda? "))
                if DCof >= 1:
                    PesananCair['Dalgona Coffee'] = DCof
                    HargaTotal += 4 * DCof
                    Minuman += DCof
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()
            
            elif DrinkChoice == "3":
                if 'Mixed Fruits Juice' in PesananCair:
                    HargaTotal -= 2 * MXJuice
                    Minuman -= MXJuice
                    PesananCair.pop('Mixed Fruits Juice') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                MXJuice = int(input(" Berapa banyak pesanan Anda? "))
                if MXJuice >= 1:
                    PesananCair['Mixed Fruits Juice'] = MXJuice
                    HargaTotal += 2 * MXJuice
                    Minuman += MXJuice
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()
            
            elif DrinkChoice == "4":
                if 'Mixed Veggies Juice' in PesananCair:
                    HargaTotal -= 2 * MVJuice
                    Minuman -= MVJuice
                    PesananCair.pop('Mixed Veggies Juices') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                MVJuice = int(input(" Berapa banyak pesanan Anda? "))
                if MVJuice >= 1:
                    PesananCair['Mixed Veggies Juice'] = MVJuice
                    HargaTotal += 2 * MXJuice
                    Minuman += MXJuice
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()
            
            elif DrinkChoice == "5":
                if 'Thai Tea' in PesananCair:
                    HargaTotal -= 4 * TTea
                    Minuman -= TTea
                    PesananCair.pop('Thai Tea') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                TTea = int(input(" Berapa banyak pesanan Anda?"))
                if TTea >= 1:
                    PesananCair['Thai Tea'] = TTea
                    HargaTotal += 4 * TTea 
                    Minuman += TTea
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif DrinkChoice == "6":
                if 'White Coffee' in PesananCair:
                    HargaTotal -= 3 * WCof 
                    Minuman -= WCof
                    PesananCair.pop('White Coffee') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                WCof = int(input(" Berapa banyak pesanan Anda? "))
                if WCof >= 1:
                    PesananCair['White Coffee'] = WCof
                    HargaTotal += 3 * WCof
                    Minuman += WCof
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()
            
            elif DrinkChoice == "7":
                if 'Irish Coffee' in PesananCair:
                    HargaTotal -= 4 * ICof 
                    Minuman -= ICof
                    PesananCair.pop('Irish Coffee') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                ICof = int(input(" Berapa banyak pesanan Anda? "))
                if ICof >= 1:
                    PesananCair['Irish Coffee'] = ICof
                    HargaTotal += 4 * ICof
                    Minuman += ICof
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif DrinkChoice == "8":
                if 'Caffe Lattee' in PesananCair:
                    HargaTotal -= 3 * CLatte
                    Minuman -= CLatte
                    PesananCair.pop('Caffe Latte') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                CLatte = int(input(" Berapa banyak pesanan Anda? "))
                if CLatte >= 1:
                    PesananCair['Caffe Latte'] = CLatte
                    HargaTotal += 3 * CLatte
                    Minuman += CLatte
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif DrinkChoice == "9":
                if 'Espresso Macchiato' in PesananCair:
                    HargaTotal -= 3 * EMac
                    Minuman -= EMac
                    PesananCair.pop('Espresso Macchiato') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                EMac = int(input(" Berapa banyak pesanan Anda? "))
                if EMac >= 1:
                    PesananCair['Espresso Macchiato'] = EMac
                    HargaTotal += 3 * EMac
                    Minuman += EMac
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif DrinkChoice == "10":
                if 'Lemon Squash' in PesananCair:
                    HargaTotal -= 3 * LSqua
                    Minuman -= LSqua
                    PesananCair.pop('Lemon Squash') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                LSqua = int(input(" Berapa banyak pesanan Anda? "))
                if LSqua >= 1:
                    PesananCair['Lemon Squash'] = LSqua
                    HargaTotal += 3 * LSqua
                    Minuman += LSqua
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif DrinkChoice == "11":
                if 'O (Coffee)' in PesananCair:
                    HargaTotal -= 2 * OCof 
                    Minuman -= OCof
                    PesananCair.pop('O (Coffee)') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                OCof = int(input(" Berapa banyak pesanan Anda? "))
                if OCof >= 1:
                    PesananCair['O (Coffee)'] = OCof
                    HargaTotal += 2 * OCof
                    Minuman += OCof
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()
            
            elif DrinkChoice == "12":
                if 'Valencia Fizz' in PesananCair:
                    HargaTotal -= 3 * VFizz 
                    Minuman -= VFizz
                    PesananCair.pop('Valencia Fizz') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                VFizz = int(input(" Berapa banyak pesanan Anda? "))
                if VFizz >= 1:
                    PesananCair['Valencia Fizz'] = VFizz
                    HargaTotal += 3 * VFizz 
                    Minuman += VFizz
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif DrinkChoice == "13":
                if 'Electrolyte Drinks' in PesananCair:
                    HargaTotal -= 7 * EDrink
                    Minuman -= EDrink
                    PesananCair.pop('Electrolyte Drinks') 
                print("\n\033[0;33;40m V: \"Mohon ketik dengan angka atau sistem kami akan melakukan usir paksa..\"\033[0;37;40m")
                EDrink = int(input(" Berapa banyak pesanan Anda? "))
                if EDrink >= 1:
                    PesananCair['Electrolyte Drinks'] = EDrink
                    HargaTotal += 7 * EDrink
                    Minuman += EDrink
                    print(" Pesanan Ditambahkan!")
                    input()
                clear()

            elif DrinkChoice.casefold() == "kembali" or DrinkChoice == "0" :
                clear()
                break

            else:
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
                MenuAwal += 1
                break

            elif GrandFinale.casefold() == "no" or GrandFinale.casefold() == "tidak" or GrandFinale.casefold() == "n":
                clear()
                break
            else:
                print("\n\033[0;33;40m V: \"Mohon ketik \"yes\" atau \"no\"\"\033[0;37;40m")
                input()

    else:        
        print("\n\033[0;33;40m V: \"Menunya gaada.. (atau belum ada?)\"\033[0;37;40m")
        input()
        clear()

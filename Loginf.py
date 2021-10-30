from os import system

#2109106039

def clear():
    _ = system('cls')

_ = system('')

Data = dict([("Viabel","VeriveryNice"),("Alibaba","Super")])
Home = 0
a = 0
b = 0
c = 0
Salah = 0

def banner():
    print("\033[0;37;46m", "(O)" * 30, "\033[0;37;40m ~")

while Home == 0:
    if Salah == 3:
        break
    clear()
    banner()
    print("\n Selamat Datang, Sahabat:")
    SignIn = str(input(" [1] Login\t [2] Sign Up\t [3] Out  --> "))
    if SignIn == "1":
        a = 0
        b = 0
        while a == 0 and Salah < 3:
            UsnCheck = str(input("\tUsername: \033[0;36;40m"))
            if UsnCheck in Data:
                while b == 0:
                    PassCheck = str(input("\t\033[0;37;40mPassword: \033[0;36;40m"))
                    if (UsnCheck, PassCheck) in Data.items():
                        while c == 0:
                            Salah = 0
                            clear()
                            banner()
                            print(f"\n\t\t\033[0;37;40mSelamat Datang \033[0;36;40m{UsnCheck}\033[0;37;40m!!!")
                            print("""
                    [1] Ubah Username
                    [2] Ubah Password
                    [3] Log Out""")
                            print("\t\t\033[1;37;42m\n Aplikasi ini masih versi LITE, lakukan pembayaran untuk menu lainnya \033[1;37;40m")
                            Opsi = str(input("\n\n Pilih: \033[0;36;40m"))
                            print("\033[0;37;40m\n")

                            if Opsi == "1":
                                UsnChecker = str(input(" Masukkan Username baru:\033[0;36;40m "))
                                CheckingUSN = len(UsnChecker)
                                if CheckingUSN <= 1:
                                    print("\t\t\033[0;37;40m Mohon Isi Usernamemu")
                                    input()
                                    clear()
                                    continue
                                if UsnChecker in Data:
                                    print("\t\t\033[0;37;40m Username tidak dapat dipakai karena sudah ada")
                                    input()
                                    clear()
                                    print("\n\n\n")
                                else:
                                    Data.pop(UsnCheck)
                                    print("\033[0;32;40m Username Diperbarui\033[0;37;40m")
                                    Data[UsnChecker] = PassCheck
                                    UsnCheck = UsnChecker
                                    input()

                            elif Opsi == "2":
                                PasswordC = str(input(" Masukkan Password lama:\033[0;36;40m "))
                                if PassCheck == PasswordC:
                                    PassChecker = str(input(" \033[0;37;40mMasukkan Password Baru:\033[0;36;40m "))
                                    Censor = len(PassChecker)
                                    if Censor <= 1:
                                        print(" \033[0;37;40mMohon Masukkan Password")
                                        input()
                                        clear()
                                        continue
                                    while a == 0:
                                        NewPasswordC = str(input("\033[0;37;40m Masukkan ulang password Anda: \033[0;36;40m"))
                                        if PassChecker != NewPasswordC :
                                            print("\033[0;37;40m Password Tidak Sesuai.")
                                            input()
                                            clear()
                                            banner()
                                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                        else:
                                            Data.pop(UsnCheck)
                                            Data[UsnCheck] = PassChecker
                                            PassCheck = PassChecker
                                            print("\033[0;32;40m Password Diperbaharui!\033[0;37;40m")
                                            input()
                                            clear()
                                            break
                                        break
                                        
                                else:
                                    print("\033[0;31;40m Penggantian Password Gagal!\033[0;37;40m")
                                    input()
                            elif Opsi == "3":
                                a += 1
                                b += 1
                                clear()
                                break
                            

                    elif (UsnCheck, PassCheck) not in Data.items():
                        if Salah < 2:
                            clear()
                            banner()
                            Salah += 1
                            print(" \033[0;31;40mPassword yang Anda masukkan salah")
                            print(" Max Sandi salah adalah 3 kali, Anda telah salah",Salah,"kali\033[1;37;40m")
                            print("\n\n\n\t\033[0;37;40mUsername:\033[0;36;40m",UsnCheck)
                        else:
                            print("\033[1;31;40m\tSelamat Tinggal\033[0;37;40m")
                            input()
                            quit()

            elif UsnCheck not in Data:
                print ("\t\033[0;37;40mUsername Tidak Ditemukan")
                input()
                clear()

                break
    elif SignIn == "2":
        a = 0
        while a == 0:
            NewUsername = str(input("\t Masukkan Username yang diinginkan:\033[0;36;40m\t "))
            CheckingUSN = len(NewUsername)
            if CheckingUSN <= 1:
                print("\t\t\033[0;37;40m Mohon Isi Usernamemu")
                input()
                clear()
                banner()
                print("\n\n")
                continue
            if NewUsername in Data:
                print("\t\t\033[0;37;40m Username tidak dapat dipakai karena sudah ada")
                input()
                clear()
                print("\n\n\n")
            else:
                while a == 0:
                    NewPassword = str(input("\t\033[0;37;40m Masukkan password yang diinginkan:\033[0;36;40m\t "))
                    Censor = len(NewPassword)
                    if Censor <= 1:
                        print(" \033[0;37;40mMohon Masukkan Password")
                        input()
                        clear()
                        banner()
                        print("\n\n\n\t\033[0;37;40m Masukkan Username yang diinginkan:\t\033[0;36;40m",NewUsername)
                        continue
                    clear()
                    while a == 0:
                        print("\n\n\n\t\033[0;37;40mUsername:\t\033[0;36;40m",NewUsername)
                        print("\t\033[0;37;40mPassword:\t\033[0;36;40m","*" * Censor)
                        NewPasswordC = str(input("\t\033[0;37;40mMasukkan ulang password Anda:\t \033[0;36;40m"))
                        if NewPassword != NewPasswordC:
                            print("\033[0;37;40m Password Tidak Sesuai.")
                            input()
                            clear()
                        else:
                            Data[NewUsername] = NewPassword
                            print("\033[0;32;40m Sign Up berhasil!\033[0;37;40m")
                            input()
                            clear()
                            a += 1
                            break
    elif SignIn == "3":
        break

    else:
        print(" Menu tidak tersedia")
        input()
        clear()
from F01 import *
from F02 import *
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F14 import *
from F15 import *
from F17 import *


loginStatus, userActive, userRole = login(File1, loginStatus, userActive)

while loginStatus == False:
    opsi = input("\nIngin login ulang? (y/n) ")
    if opsi == "Y" or opsi == "y":
        loginStatus, userActive, userRole = login(File1, loginStatus, userActive)
    elif opsi == "N" or opsi == "n":
        break
    else:
        print("Masukan tidak valid!")

while loginStatus == True:
    print(">>>", end=" ")
    opsi = input()
    if opsi == "register":
        if userRole == 'Admin':
            register(dataFile1)
        else:
            print("Hanya bisa diakses Admin!")
    elif opsi == "carirarity":
        R = input("Masukkan rarity: ")
        print("\nHasil Pencarian: ")
        carirarity(R,dataFile2)
    elif opsi == "caritahun":
        tahun = int(input("Masukkan tahun: "))
        category = input("Masukkan kategori: ")
        print("\nHasil Pencarian: ")
        caritahun(tahun,category,dataFile2)
    elif opsi == "tambahitem":
        if userRole == 'Admin':
            ID = str(input("Masukan ID: "))
            tambahitem(dataFile2,dataFile3,ID)
        else:
            print("Hanya bisa diakses Admin!")
    elif opsi == "hapusitem":
        if userRole == 'Admin':
            ID = str(input("Masukan ID: "))
            hapusitem(dataFile2,dataFile3,ID)
        else:
            print("Hanya bisa diakses Admin!")
    elif opsi == "ubahjumlah":
        if userRole == 'Admin':
            ID = str(input("Masukan ID: "))
            ubahjumlah(dataFile2,dataFile3,ID)
        else:
            print("Hanya bisa diakses Admin!")
    elif opsi == "pinjam":
        continue
    elif opsi == "kembalikan":
        continue
    elif opsi == "minta":
        continue
    elif opsi == "riwayatpinjam":
        continue
    elif opsi == "riwayatkembali":
        continue
    elif opsi == "riwayatambil":
        continue
    elif opsi == "status":
        print(loginStatus)          # Apapun yg ingin diamati saat tes code
        print(userActive)           # HAPUS bagian ini sebelum dikumpul
        print(userRole)
        print(File1)
        print(headerFile1)
        print(dataFile1)
    elif opsi == "save":
        folder_penyimpanan = input("Masukkan nama folder penyimpanan: ")
        save(folder_penyimpanan)
    elif opsi == "help":
        continue
    elif opsi == "exit":
        exit()
        loginStatus = False
    else:
        print("opsi tidak tersedia!")

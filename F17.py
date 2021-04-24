from F14 import *
from F15 import *

def exit():
    while True:
        isSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if isSave == "Y" or isSave == "y":
            folder_penyimpanan = input("Masukkan nama folder penyimpanan: ")
            save(folder_penyimpanan)
            print("Saving. . .")
            break
        elif isSave == "N" or isSave == "n":
            break
        else:
            print("Masukan tidak valid!")
            continue



def ubahjumlah(gadgetdatas,consumdatas,ID):
    Found = False
    if (ID[0] == 'G'):
        for i in range (len(gadgetdatas)):
            if (ID == gadgetdatas[i][0]):
                Found = True
                print(gadgetdatas[i][1])
                jumlah = int(input("Masukkan Jumlah: "))
                hasil = int(gadgetdatas[i][3]) + jumlah
                if (hasil > 0):
                    gadgetdatas[i][3] = hasil
                    if (jumlah > 0):
                        print("\n"+ str(jumlah) + " " + gadgetdatas[i][1] + " berhasil ditambahkan. Stok sekarang: " + str(hasil))
                    elif (jumlah < 0):
                        print("\n"+ str(-jumlah) + " " + gadgetdatas[i][1] + " berhasil dibuang. Stok sekarang: " + str(hasil))
                    else:
                        print("\njumlah " + gadgetdatas[i][1] + " tetap. Stok sekarang: " + str(hasil) )
                else:
                    if (jumlah > 0):
                        print("\n"+ str(jumlah) + " " + gadgetdatas[i][1] + " gagal dibuang karena stok kurang. Stok sekarang: " + int(gadgetdatas[i][3]) + " (< " + str(jumlah) + ")")
                    else:
                        print("\n"+ str(-jumlah) + " " + gadgetdatas[i][1] + " gagal dibuang karena stok kurang. Stok sekarang: " + int(gadgetdatas[i][3]) + " (< " + str(-jumlah) + ")")
        if (Found == False):
            print("Tidak ada item dengan ID tersebut!")
    elif (ID[0] == 'C'):
        for i in range (len(consumdatas)):
            if (ID == consumdatas[i][0]):
                Found = True
                jumlah = int(input("Masukkan Jumlah: "))
                hasil = int(consumdatas[i][3]) + jumlah
                if (hasil > 0):
                    consumdatas[i][3] = hasil
                    if (jumlah > 0):
                        print("\n"+ str(jumlah) + " " + consumdatas[i][1] + " berhasil ditambahkan. Stok sekarang: " + str(hasil))
                    elif (jumlah < 0):
                        print("\n"+ str(-jumlah) + " " + consumdatas[i][1] + " berhasil dibuang. Stok sekarang: " + str(hasil))
                    else:
                        print("\njumlah " + consumdatas[i][1] + " tetap. Stok sekarang: " + str(hasil) )
                else:
                    if (jumlah > 0):
                        print("\n"+ str(jumlah) + " " + consumdatas[i][1] + " gagal dibuang karena stok kurang. Stok sekarang: " + int(consumdatas[i][3]) + " (< " + str(jumlah) + ")")
                    else:
                        print("\n"+ str(-jumlah) + " " + consumdatas[i][1] + " gagal dibuang karena stok kurang. Stok sekarang: " + int(consumdatas[i][3]) + " (< " + str(-jumlah) + ")")
        if (Found == False):
            print("Tidak ada item dengan ID tersebut!")
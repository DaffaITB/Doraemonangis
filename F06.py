def hapusitem(gadgetdatas,consumdatas,ID):
    Found = False
    if (ID[0] == 'G'):
        for i in range (len(gadgetdatas)):
            if (ID == gadgetdatas[i][0]):
                Found = True
                pil = input("Apakah anda yakin ingin menghapus " + gadgetdatas[i][1] + " (Y/N)?")
                if (pil == 'Y'):
                    gadgetdatas[i:i+1] = []
                    print("\nItem telah berhasil dihapus dari database.")
                else:
                    print("Item tidak dihapus dari database")
        if (Found == False):
            print("Tidak ada item dengan ID tersebut.")
    elif (ID[0] == 'C'):
        for i in range (len(consumdatas)):
            if (ID == consumdatas[i][0]):
                Found = True
                pil = input("Apakah anda yakin ingin menghapus " + consumdatas[i][1] +" (Y/N)?")
                if (pil == 'Y'):
                    consumdatas[i:i+1] = []
                    print("\nItem telah berhasil dihapus dari database.")
                else:
                    print("Item tidak dihapus dari database")
        if (Found == False):
            print("Tidak ada item dengan ID tersebut.")
    else:
        print("Tidak ada item dengan ID tersebut.")
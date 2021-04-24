def modifygadgetdata(gadgetdatas,ID):
    Found = False
    for i in range (len(gadgetdatas)):
        if (ID == gadgetdatas[i][0]):
            Found = True
    if (Found == False):
        nama = input("Masukan Nama: ")
        desk = input("Masukan Deskripsi: ")
        jumlah = input("Masukan Jumlah: ")
        rarity = input("Masukan Rarity: ")
        if (rarity == 'C' or rarity == 'B' or rarity == 'A' or rarity == 'S'):
            tahun = input("Masukan tahun ditemukan: ") 
            newdata = [ID,nama,desk,jumlah,rarity,tahun] 
            gadgetdatas.append(newdata)
            print("Item telah berhasil ditambahkan")
        else:
            print("Input rarity tidak valid!")
    else:
        print("Gagal menambahkan karena ID sudah ada")  

def modifyconsumdata(consumdatas,ID):
    Found = False
    for i in range (len(consumdatas)):
        if (ID == consumdatas[i][0]):
            Found = True
    if (Found == False):
        nama = input("Masukan Nama: ")
        desk = input("Masukan Deskripsi: ")
        jumlah = input("Masukan Jumlah: ")
        rarity = input("Masukan Rarity: ")
        if (rarity == 'C' or rarity == 'B' or rarity == 'A' or rarity == 'S'):
            newdata = [ID,nama,desk,jumlah,rarity] 
            consumdatas.append(newdata)
            print("Item telah berhasil ditambahkan")
        else:
            print("Input rarity tidak valid!")
    else:
        print("Gagal menambahkan karena ID sudah ada")       
            
def tambahitem(gadgetdatas,consumdatas,ID):
    if (ID[0] == 'G'):
        modifygadgetdata(gadgetdatas,ID)
    elif (ID[0] == 'C'):
        modifyconsumdata(consumdatas,ID)
    else:
        print("Gagal menambahkan item karena ID tidak valid")
def printdata(i):
    print("\nNama             :",i[1])
    print("Deskripsi        :",i[2])
    print("Jumlah           :",i[3],"buah")
    print("Rarity           :",i[4])
    print("Tahun Ditemukan  :",i[5])
    
def carirarity(R,gadgetdatas):
    Found = False
    valid = True
    for i in gadgetdatas :
        if (R == 'A' and i[4] == 'A'):
            printdata(i)
            Found = True
        elif (R == 'B' and i[4] == 'B'):
            printdata(i)
            Found = True
        elif (R == 'C' and i[4] == 'C'):
            printdata(i)
            Found = True
        elif (R == 'S' and i[4] == 'S'):
            printdata(i)
            Found = True
        elif (R != 'A' and R != 'B' and R != 'C' and R != 'S'):
            valid = False
    if (valid == False):
        print("Rarity tidak valid!")
    elif (Found == False and valid == True):
        print("Tidak ada item dengan rarity tersebut.")
            
    
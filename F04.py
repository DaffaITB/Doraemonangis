def printdata(i):
    print("\nNama             :",i[1])
    print("Deskripsi        :",i[2])
    print("Jumlah           :",i[3],"buah")
    print("Rarity           :",i[4])
    print("Tahun Ditemukan  :",i[5])
    
def caritahun(tahun,category,gadgetdatas):
    Found = False
    for i in gadgetdatas :
        if (category == '=' and i[5] == tahun):
            printdata(i)
            Found = True
        elif (category == '>' and i[5] > tahun):
            printdata(i)
            Found = True
        elif (category == '<' and i[5] < tahun):
            printdata(i)
            Found = True
        elif (category == '<=' and i[5] <= tahun):
            printdata(i)
            Found = True
        elif (category == '>=' and i[5] >= tahun):
            printdata(i)
            Found = True
    if (Found == False):
        print("Tidak ada item dengan tahun tersebut.")
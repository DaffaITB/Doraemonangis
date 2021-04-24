def register(dataUser):
    dataBaru = []
    id       = len(dataUser) + 1
    role     = "User"
    nama     = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    alamat   = input("Masukkan alamat: ")

    print("User", username, "telah berhasil register ke dalam Kantong Ajaib.")

    dataBaru = [id, username, nama, alamat, password, role]
    dataUser.append(dataBaru)
    print(dataBaru)
    print(dataUser)
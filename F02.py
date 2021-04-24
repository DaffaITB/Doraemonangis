loginStatus = False
userActive = None
userRole = None

def login(dataUser, loginStatus, userActive):
    if loginStatus == True:
        print("Anda sudah login!")
        return loginStatus, userActive, userRole
    else:
        username = input("\nMasukan username: ")
        password = input("Masukan password: ")
        for i in range(len(dataUser)):
            if dataUser[i][1] == username and dataUser[i][4] == password:
                print("\nHalo", username + "!", "Selamat datang di Kantong Ajaib\n")
                loginStatus = True
                userActive = username
                userRole = dataUser[i][5]
                return loginStatus, userActive, userRole
                break
            elif i == (len(dataUser)-1):
                print("username tidak terdaftar atau password tidak cocok!")
                userRole = None
                return loginStatus, userActive, userRole
            else:
                continue
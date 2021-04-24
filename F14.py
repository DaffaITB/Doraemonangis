import os
import argparse

parser = argparse.ArgumentParser(description='Parser description')
parser.add_argument("folder", help='Folder penyimpanan data')
args = parser.parse_args()

address = str(os.path.abspath(os.getcwd())) + "\\" + str(args.folder)
if args.folder:
    print("\nLoading...\n")
    print('Selamat datang di "Kantong Ajaib!"')
else:
    print("Tidak ada nama folder yang diberikan!")

#Pengolahan file menjadi data siap pakai====================================
File1 = open(str(address)+ "\\" + "user.csv","r")
raw_F1 = File1.readlines()
File1.close()

File2 = open(str(address)+ "\\" +"gadget.csv","r")
raw_F2 = File2.readlines()
File2.close()

File3 = open(str(address)+ "\\" +"consumable.csv","r")
raw_F3 = File3.readlines()
File3.close()

File4 = open(str(address)+ "\\" +"consumable_history.csv","r")
raw_F4 = File4.readlines()
File4.close()

File5 = open(str(address)+ "\\" +"gadget_borrow_history.csv","r")
raw_F5 = File5.readlines()
File5.close()

File6 = open(str(address)+ "\\" +"gadget_return_history.csv","r")
raw_F6 = File6.readlines()
File6.close()

File1 = [raw_line.replace("\n", "") for raw_line in raw_F1]
File2 = [raw_line.replace("\n", "") for raw_line in raw_F2]
File3 = [raw_line.replace("\n", "") for raw_line in raw_F3]
File4 = [raw_line.replace("\n", "") for raw_line in raw_F4]
File5 = [raw_line.replace("\n", "") for raw_line in raw_F5]
File6 = [raw_line.replace("\n", "") for raw_line in raw_F6]

#Fungsi pencacah/perapih data==========================================================
def convert_array_data_to_real_values(arr, headerFile) :
    arr_cpy = arr[:]
    for i in range(len(headerFile)) :
        try:
            arr_cpy[i] = int(arr_cpy[i])
        except:
            continue
    return arr_cpy

def parser(line):
    data = []
    arr_char = []
    list = ""
    for string in line:
        for char in string:
            #print(char)
            arr_char.append(char)
    for i in range (len(arr_char)):
        if (arr_char[i] != ';'):
            list += arr_char[i]
            if (i == (len(arr_char)-1)):
                data[i:] = [list]
            else:
                i += 1
        else:
            data[i:] = [list]
            i += 1
            list = ""
    return data

def convert_line_to_data(line) :
    raw_array_of_data = parser(line)
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
#======================================================================================

headerFile1 = File1.pop(0)
headerFile1 = convert_line_to_data(headerFile1)
dataFile1 = []
for line in File1:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data, line)
    dataFile1.append(real_values)

headerFile2 = File2.pop(0)
headerFile2 = convert_line_to_data(headerFile2)
dataFile2 = []
for line in File2:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data, line)
    dataFile2.append(real_values)

headerFile3 = File3.pop(0)
headerFile3 = convert_line_to_data(headerFile3)
dataFile3 = []
for line in File3:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data, line)
    dataFile3.append(real_values)

headerFile4 = File4.pop(0)
headerFile4 = convert_line_to_data(headerFile4)
dataFile4 = []
for line in File4:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data, line)
    dataFile4.append(real_values)

headerFile5 = File5.pop(0)
headerFile5 = convert_line_to_data(headerFile5)
dataFile5 = []
for line in File5:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data, line)
    dataFile5.append(real_values)

headerFile6 = File6.pop(0)
headerFile6 = convert_line_to_data(headerFile6)
dataFile6 = []
for line in File6:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data, line)
    dataFile6.append(real_values)

#File hasil siap pakai
File1 = [headerFile1] + dataFile1
File2 = [headerFile2] + dataFile2
File3 = [headerFile3] + dataFile3
File4 = [headerFile4] + dataFile4
File5 = [headerFile5] + dataFile5
File6 = [headerFile6] + dataFile6
import os
from F14 import *

def convert_datas_to_string(header, data) :
    string_data = ";".join(header) + "\n"
    for arr_data in data:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def create_folder(folder):
    try:
        os.mkdir(os.path.abspath(os.getcwd()) + "//" + folder)
    except FileExistsError:
        None

def save(folder):
    create_folder(folder)
    WriteFile1 = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "user.csv","w")
    WriteFile2 = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "gadget.csv","w")
    WriteFile3 = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "consumable.csv","w")
    WriteFile4 = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "consumable_history.csv","w")
    WriteFile5 = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "gadget_borrow_history.csv","w")
    WriteFile6 = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "gadget_return_history.csv","w")
    
    WriteFile1.write(convert_datas_to_string(headerFile1, dataFile1))
    WriteFile2.write(convert_datas_to_string(headerFile2, dataFile2))
    WriteFile3.write(convert_datas_to_string(headerFile3, dataFile3))
    WriteFile4.write(convert_datas_to_string(headerFile4, dataFile4))
    WriteFile5.write(convert_datas_to_string(headerFile5, dataFile5))
    WriteFile6.write(convert_datas_to_string(headerFile6, dataFile6))

    WriteFile1.close()
    WriteFile2.close()
    WriteFile3.close()
    WriteFile4.close()
    WriteFile5.close()
    WriteFile6.close()
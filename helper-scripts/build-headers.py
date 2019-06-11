#Builds header src files

import os
ROOT = os.getcwd()

headers = os.listdir(ROOT + "\\include\\BankSystem")

for h in headers:
    h_name = h[:-4]    
    file_path = ".\\src\\" + h_name + ".cpp"
    if os.path.isfile(file_path):
        cmd = "g++ -c -o .\\build\\" + h_name + ".o " + file_path
        os.system(cmd)
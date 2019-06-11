#Builds header src files

import os

ROOT = os.getcwd()

headers = os.listdir(ROOT + os.sep+"include"+os.sep+"BankSystem")

for h in headers:
    h_name = h[:-4]    
    file_path = "."+os.sep+"src"+os.sep + h_name + ".cpp"
    if os.path.isfile(file_path):
        cmd = "g++ -c -o ."+os.sep+"build"+os.sep+ h_name + ".o " + file_path
        os.system(cmd)
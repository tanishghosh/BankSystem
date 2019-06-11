#Clears build and generated executable

import os

ROOT = os.getcwd()

build_files = os.listdir(ROOT + ""+os.sep+"build")

build_files.remove(".gitkeep")

for o in build_files:
    file_path = ROOT + ""+os.sep+"build"+os.sep+"" + o
    if os.path.isfile(file_path):
        os.unlink(file_path)

file_path = ROOT + ""+os.sep+"bin"+os.sep+"" + "a.exe"

if os.path.isfile(file_path):
    os.unlink(file_path)

file_path = ROOT + ""+os.sep+"bin"+os.sep+"" + "a.out"


if os.path.isfile(file_path):
    os.unlink(file_path)
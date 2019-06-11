#Clears build and generated executable

import os

ROOT = os.getcwd()

build_files = os.listdir(ROOT + "\\build")

build_files.remove(".gitkeep")

for o in build_files:
    file_path = ROOT + "\\build\\" + o
    if os.path.isfile(file_path):
        os.unlink(file_path)

file_path = ROOT + "\\bin\\" + "a.exe"

if os.path.isfile(file_path):
    os.unlink(file_path)

file_path = ROOT + "\\bin\\" + "a.out"


if os.path.isfile(file_path):
    os.unlink(file_path)
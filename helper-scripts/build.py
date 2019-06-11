#Builds main src file

import os
ROOT = os.getcwd()

cmd = "g++ -c -o .\\build\\main.o .\\src\\main.cpp"
os.system(cmd)

objects = os.listdir(ROOT + "\\build")
cmd = "g++  -o .\\bin\\a"

objects.remove(".gitkeep")

for o in objects:
    cmd += " .\\build\\" + o

os.system(cmd)
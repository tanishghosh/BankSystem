#Builds main src file

import os

ROOT = os.getcwd()

cmd = "g++ -c -o ."+os.sep+"build"+os.sep+"main.o ."+os.sep+"src"+os.sep+"main.cpp"
os.system(cmd)

objects = os.listdir(ROOT + ""+os.sep+"build")
cmd = "g++  -o ."+os.sep+"bin"+os.sep+"a"

objects.remove(".gitkeep")

for o in objects:
    cmd += " ."+os.sep+"build"+os.sep+"" + o

os.system(cmd)
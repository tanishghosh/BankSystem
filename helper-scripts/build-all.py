#Builds all src files

import os

cmd = "python .\\helper-scripts\\build-headers.py"
os.system(cmd)

cmd = "python .\\helper-scripts\\build.py"
os.system(cmd)
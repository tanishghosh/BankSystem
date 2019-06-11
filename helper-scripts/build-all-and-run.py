#Builds all src files and executes the application

import os

cmd = "python .\\helper-scripts\\build-all.py"
os.system(cmd)

cmd = "python .\\helper-scripts\\run.py"
os.system(cmd)
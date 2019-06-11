#Builds main src file and executes the application

import os

cmd = "python .\\helper-scripts\\build.py"
os.system(cmd)

cmd = "python .\\helper-scripts\\run.py"
os.system(cmd)
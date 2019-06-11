#Builds main src file and executes the application

import os

cmd = "python ."+os.sep+"helper-scripts"+os.sep+"build.py"
os.system(cmd)

cmd = "python ."+os.sep+"helper-scripts"+os.sep+"run.py"
os.system(cmd)
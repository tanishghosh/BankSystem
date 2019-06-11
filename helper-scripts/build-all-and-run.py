#Builds all src files and executes the application

import os
  
cmd = "python ."+os.sep+"helper-scripts"+os.sep+"build-all.py"
os.system(cmd)

cmd = "python ."+os.sep+"helper-scripts"+os.sep+"run.py"
os.system(cmd)
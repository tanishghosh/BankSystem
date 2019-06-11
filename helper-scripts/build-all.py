#Builds all src files

import os
  
cmd = "python ."+os.sep+"helper-scripts"+os.sep+"build-headers.py"
os.system(cmd)

cmd = "python ."+os.sep+"helper-scripts"+os.sep+"build.py"
os.system(cmd)
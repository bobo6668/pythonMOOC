#batchInstall.py

import os

libs = {"numpy", "matplotlib"}

try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Successful")
except:
    print("Failed Somehow")
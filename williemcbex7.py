import os
import shelve
import sys
import pyperclip as pp

from williemcbex3 import getKey

os.chdir ("/home/alvinh/Documents/Python/PyScratchSpace")
print(os.getcwd())

data = shelve.open("mcb")

if sys.argv[1] == "save":
    getKey = sys.argv[2]
    data[getKey] = pp.paste()
else:
    getKey = sys.argv[1]
    pp.copy("hard coded")
    print(pp.paste())
    # pp.copy(data[getKey])

data.close()

# data[getKey] = getValue
# print(data)

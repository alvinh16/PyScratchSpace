import os
import shelve
import sys
import pyperclip as pp

os.chdir ("/home/alvinh/Documents/Python/PyScratchSpace")
print(os.getcwd())

data = shelve.open("mcb")

getKey = sys.argv[1]
getValue = pp.paste()
data[getKey] = getValue
print(list(data.keys()))
print(list(data.values()))

data.close()

# data[getKey] = getValue
# print(data)

import os
import shelve
import pyperclip as pp

os.chdir ("/home/alvinh/Documents/Python/PyScratchSpace")
print(os.getcwd())
data = shelve.open("mcb")

getKey = input("Enter in key : ")
getValue = pp.paste()
print(list(data.keys()))
print(list(data.values()))

data.close()

# data[getKey] = getValue
# print(data)

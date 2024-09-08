import os
import shelve
import sys
import pyperclip as pp

# from williemcbex3 import getKey

os.chdir ("/home/alvinh/Documents/Python/PyScratchSpace")
print(os.getcwd())

data = shelve.open("mcb")

if sys.argv[1] == "save":
    print(f"Saving {sys.argv[2]}")
    getKey = sys.argv[2]
    data[getKey] = pp.paste()
else:
    getKey = sys.argv[1]
    print(f"Getting {getKey}")
    # pp.copy("hard coded")
    # print(pp.paste())
    print(f"getKey: {getKey}")
    print(f"data: {data}")
    print(f"data[getKey]: {data[getKey]}")
    print(f"NOW I'm copying")
    pp.copy(data[getKey])
    print(data[getKey])

data.close()

# data[getKey] = getValue
# print(data)

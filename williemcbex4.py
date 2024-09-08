import pyperclip as pp

data = {}
getKey = input("Enter in key : ")
getValue = pp.paste()

data[getKey] = getValue
print(data)

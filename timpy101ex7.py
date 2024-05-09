#!/usr/bin/python3

x = [i for i in range (10)]

print (x)
print ("omit the 1st cell, ", x[1:])
print ("print only the last cell, ", x[-1:])
print ("omit alternate cells, ", x[::2])
print ("alternate even cells, ", x[1::2])
print ("print all cells, halt at the 3rd from the last, ", x[:-3])
print ("print alt cells, halt at the 3rd from the last, ", x[:-3:2])
print ("print alt even cells, halt at the 3rd from the last, ", x[1:-3:2])

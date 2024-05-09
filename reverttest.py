#!/usr/bin/python3

rawlist = input ("input list of objects separated by space : ")
print ("you have entered,")
print ()
print (rawlist)

cook = rawlist.split(" ")
n = len(cook)
print ("the list is ", n, " long.")
print ("the objects are, ")
for i in range (0,n):
     print (cook[i])

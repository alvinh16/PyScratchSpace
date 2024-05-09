#!/usr/bin/python3
objlist = []
def getobjects():

    rawlist = input ("Please give list of objects separated by white space character : ")
    rawlist = rawlist.split(" ")
    return rawlist

objlist = getobjects()
print ("the list is, ", objlist)

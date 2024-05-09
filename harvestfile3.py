#!/usr/bin/python3
#
# This program uses an index sort method
# to put an randomly ordered list into a sorted 
#

household = []

def GetObj():
# This procedue reads from the input file, objectlist.text
# & populates the list household
#
     source_file = open("objectlist.text", "r")
     Organize = source_file.readlines()
     i=0
     for words in Organize :
          household.append(words.rstrip("\r\n"))
          i += 1
     source_file.close()
     return(household)

def DispObj(rows):
# This procedure dumps the content of rows on the screen
      # clear the file from prev write
      dest_file = open("sortedlist.text","w")
      top = len(rows)
      for i in range (0, top):
           dest_file.write(rows[i])
           dest_file.write("\r\n")
           print (rows[i])
      dest_file.close()

def swapcells(source, target):
    tmpobj = household[source]
    household[source] = household[target]
    household[target] = tmpobj
    print ()
#    return (newarr)

def largest(bottom):
    curr_biggest = bottom
    # what happens if position 0 is the largest?
    for i in range (0, bottom):
        # print (i)
        if household[i] > household[curr_biggest]:
                curr_biggest = i

    return curr_biggest

def bigbottom():
# a single iteration of finding
# the largest & swapping it with the  object currently
# at the bottom of the list
# swap is no necessary if the largest obj is alr at the
# bottom of the list, but the list should still b shortened
# by 1, ie the bottom of the list shd b moved up by 1 position.

     top = len(household)-1

     for i in range (top):
          print ("top= ", top)
          big = largest(top)
          if big != top :
               swapcells(largest(top), top)
          top -=1


household = GetObj()
DispObj(household)
bigbottom()

print ("the new order is")
DispObj(household)

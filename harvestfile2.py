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
    newarr = household
    tmpobj = newarr[source]
    newarr[source] = newarr[target]
    newarr[target] = tmpobj
    print ()
    return (newarr)

def largest(bottom):
    curr_biggest = 0
    big = household[curr_biggest]
    # what happens if position 0 is the largest?
    for i in range (0, bottom):
        # print (i)
        if household[i] > household[curr_biggest]:
            curr_biggest = i
    return curr_biggest

    return big


household = GetObj()
DispObj(household)

# the last cell no. is top
top = len(household)-1

# placeholder, this is a single iteration of finding
# the largest & swapping it with the  object currently
# at the bottom of the list
# swap is no necessary if the largest obj is alr at the
# bottom of the list, but the list should still b shortened
# by 1, ie the bottom of the list shd b moved up by 1 position.
household = swapcells(largest(top), top)
print ("the new order is")
DispObj(household)

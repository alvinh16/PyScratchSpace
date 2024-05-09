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
    print ("the biggest element is ", household[curr_biggest])

    return big
household = GetObj()
# DispObj(household)
DispObj(household)

top = len(household)-1
print ("the largest cell is cell no. ", top)

household = swapcells(top-1, 0)
print ("the new order is")
DispObj(household)

largest (top)
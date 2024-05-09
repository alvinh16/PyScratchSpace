#!/usr/bin/python3

def simple (lion, panther, tiger):

    print ("the value of lion is : ", lion)
    print ("the value of panther is : ", panther)
    print ("the value of tiger is : ", tiger)
    print ()
    pass

def moderate (lion, panther, tiger = None):

    print ("this is an moderate function.")
    print ("the value of lion is : ", lion)
    print ("the value of panther is : ", panther)
    print ("the value of tiger is : ", tiger)
    print ()
    pass

def mod2 (lion, panther, tiger = 10):

    print ("default for tiger is 10")
    print ("the value of lion is : ", lion)
    print ("the value of panther is : ", panther)
    print ("the value of tiger is : ", tiger)
    print ()
    pass
simple (1, 2, 3)
simple (1, tiger = 2, panther = 3)
simple (panther=1, tiger = 2, lion = 3)

moderate (9, 10)
moderate (9, 10, 8)

mod2 (9, 10)
mod2 (9, 10, 5)

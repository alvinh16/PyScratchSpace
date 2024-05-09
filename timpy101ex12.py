#!/usr/bin/python3

def tough (panther, tiger, eagle = True, falcon = False):

    print ("the value of panther is : ", panther)
    print ("the value of tiger is : ", tiger)
    print ("the value of eagle is : ", eagle)
    print ("the value of falcon is : ", falcon)
    print ()
    pass

tough (*[41, 39], **{"eagle": "hello", "falcon": "cool"})
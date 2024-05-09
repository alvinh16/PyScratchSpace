#!/usr/bin/python3

def sumof(op1, op2):

     return ( int(op1) + int(op2))

def quo(op1, op2):

     return ( float(op1) / float(op2))

def delta(op1, op2):

     return (abs(int(op1) - int(op2)))

def prod(op1, op2):
# todo : what if either op1 or 2 or both are floating point?
     return (int(op1) * int(op2))

a = input ("please give operand 1 : ")
b = input ("please give operand 2 : ")
print ("you have entered ", str(a), " and ", str(b))
print

c = sumof (a,b)
print ("the sum of ", str(a), " & ", str(b), " is ", str(c))

d = delta (a,b)
print ("the difference of ", str(a), " & ", str(b), " is ", str(d))

e = prod (a,b)
print ("the product of ", str(a), " & ", str(b), " is ", str(e))

f = quo (a,b)
print ("the quotient of ", str(a), " & ", str(b), " is ", str(f))

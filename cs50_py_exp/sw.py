#!/usr/bin/python

def sw(a , b):
    c = a
    a = b
    b = c
    print 'a-x ' + str(a)
    print 'b-y ' + str(b)

x = 12
y = 11
sw( id(x),id(y))
print 'x' + str(x)
print 'y' + str(y)

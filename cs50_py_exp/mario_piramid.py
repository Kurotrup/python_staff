#!/usr/bin/python

levels = int(raw_input('Print piramid level: '))

for i in xrange(1,levels+1):
    print ' '*(levels-i)+'*'*i+'*  *'+'*'*i

#!/usr/bin/python
'''Write a script which prints a number of polyndrom words in the dictionary
 ( polyndrom is a word that may be read the same way in either direction,
  e.g: civic, radar, level, rotor, kayak... ) '''
from os import path
from sys import exit
while True:
    ptf = raw_input('Print a file path for your dictionary where every word placed on new line: ')
    if path.exists(ptf) and path.isfile(ptf):
        fh = open(ptf)
        break
    elif path.isdir(ptf):
        print 'It`s a directory not a file! Try again\nOr type \'q\' below if you wanna exit'
    elif ptf == 'q' or ptf == 'Q': exit('Goodbye')
    else:
        print 'It`s a wrong path! Try again\nOr type \'q\' below if you wanna exit'
n = 0
for line in fh:
    line = line.strip()
    if len(line) > 1 and line == line[::-1]:
        n += 1
fh.close
print 'There are '+str(n)+' polyndrom  words in your dictionary'

#!/usr/bin/python
'''Write a script which counts words with length equal or more than 15 characters
in /etc/dictionaries-common/words  dictionary and prints the count.
NOTE: In different Linux distributions a file /etc/dictionaries-common/words may differ (even a path to this dictionary).
 So, if you have any troubles while using your version of the dictionary, please, use this one: words '''
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
    if len(line.strip()) >= 15:
        n += 1
fh.close
print 'There are '+str(n)+' words  with length equal or more than 15 characters in your dictionary'

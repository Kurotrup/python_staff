'''Write a program which asks an operator to point a full or relative path to
a text file and after that finds the longest word from it.
White space is considered as a word separator. An output should be written to
 a terminal and looks like:
longest_word - number_of_symbols
'''
from os import path
from sys import exit
while True:
    ptf = raw_input('Print a file path: ')
    if path.exists(ptf) and path.isfile(ptf):
        fh = open(ptf)
        break
    elif path.isdir(ptf):
        print 'It`s a directory not a file! Try again\nOr type \'q\' below if you wanna exit'
    elif ptf == 'q' or ptf == 'Q': exit('Goodbye')
    else:
        print 'It`s a wrong path! Try again\nOr type \'q\' below if you wanna exit'

mw = ''
mwl = 0
for line in fh:
    for w in line.split():
        if len(w) > mwl:
            mwl = len(w)
            mw = w
fh.close()
print '\"' + mw + '\"' + ' - ' + str(mwl)

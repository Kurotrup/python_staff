#!/usr/bin/python
'''
Write an interactive program which repeatedly asks to input a word and afterwards
finds a line number in the /etc/dictionaries-common/words (or here) that contains the mentioned word.
Optionally, make two solutions:
a) make your program to consume less memory ( do not load the whole "words" file in memory, process it line by line )
b) make your program to execute faster ( your may read 'words' file in memory, and use some advanced search algorithms )
'''
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
        print 'It`s a wrong path! Try again\nOr type \'q\' below if you wanna exit\n'

while True:
    word = raw_input('Print a word which position are you searching for\nOr type \'qq\' below if you wanna exit\n')
    if word and word != 'qq':
        word = word.strip()
        n = 0
        for line in fh:
            n += 1
            if word == line.strip():
                print 'The word '+ word + ' is located on the string # ' + str(n) + '\n'
                break
        else : print 'there are no such word like ' + word +' in the dictionary\n'
        fh.seek(0)
    elif word == 'qq': exit('Goodbye')
fh.close

#!/usr/bin/python
from os import path
from sys import exit
import time
# while True:
#     ptf = raw_input('Print a file path for your dictionary where every word placed on new line: ')
#     if path.exists(ptf) and path.isfile(ptf):
#         fh = open(ptf)
#         break
#     elif path.isdir(ptf):
#         print 'It`s a directory not a file! Try again\nOr type \'q\' below if you wanna exit'
#     elif ptf == 'q' or ptf == 'Q': exit('Goodbye')
#     else:
#         print 'It`s a wrong path! Try again\nOr type \'q\' below if you wanna exit'
fh = open('D:\phyton\WorkHard\Files\words_library')
while True:
    word = raw_input('Print a word which position are you searching for\nOr type \'q\' below if you wanna exit\n')

    if word and word != 'q':
        word = word.capitalize().strip()
        start = time.time()
        n = 0
        for line in fh:
            n += 1
            if word == line.strip():
                print 'The word '+ word + ' is located on string # ' + str(n) +'\n'
                print fh.tell()
                break
        else :
             print 'there are no such word like ' + word +' in the dictionary\n'
        fh.seek(0)
        end = time.time()
    elif word == 'q': exit('Goodbye')

    print end-start

fh.close

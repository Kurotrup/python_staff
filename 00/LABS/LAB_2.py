'''Modify a program from the previous task and make it find symbols that occur
 the most and the least number of times as well (letter case is significant).
Note that there are some symbols that may look weird if output them directly
 onto the screen (like newline, tab or space characters). Such symbols should
be printed with an explanation: '\n' instead or real newline, 'tab' instead of real tab symbol and so on.

An example output:

Analyzed file: './input_text.txt'
The longest word: 'Washington-on-the-Brazos'
The most frequent symbol: 'a', 20 times
The least frequent symbol: '-', 4 times
Additional (optional) subtasks:

Several different words (letters) may appear the same maximum or minimum number
of times within a file. Print all such words (letters) in the output.
Make the program to repeatedly ask a new file to analyze each time it accomplishes
 all tasks with the previous one. '''
from os import path
from sys import exit
while True:
    while True:
        ptf = raw_input('Print a file path (\'q\' for exit): ')
        if path.exists(ptf) and path.isfile(ptf):
            fh = open(ptf)
            break
        elif path.isdir(ptf):
            print 'It`s a directory not a file! Try again'
        elif ptf == 'q' or ptf == 'Q': exit('\nGoodbye\n')
        else:
            print 'It`s a wrong path! Try again'
    ltts = {}
    maxw = []
    maxwl = 0
    for line in fh:
# searching for the words with max length
        for w in line.split():
            if len(w) > maxwl:
                maxwl = len(w)
                maxw = []
                maxw.append(repr(w))
            elif len(w) == maxwl:
                maxw.append(repr(w))
# making dictionary where keys it`s symbols
# and values it`s how many times it mets
        sg = list(line)
        for w in sg:
            if w in ltts.keys():
                ltts[w] += 1
            else:
                ltts[w] = 1
    fh.close()
    print '\nAnalyzed file: ' + '\'' + ptf + '\''
    print 'The longest word(s): ' + ', '.join(maxw)
# searching for max and min values in dictionary
    maxwl = ltts[max(ltts, key=ltts.get)]
    w = ltts[min(ltts, key=ltts.get)]
    maxw = []
    mins = []
# searching for most and least frequent symbols
    for i in ltts:
        if ltts[i] == maxwl:
            maxw.append(repr(i).replace(' ',r'\s'))
        elif ltts[i] == w:
            mins.append(repr(i).replace(' ',r'\s'))
# printing
    if maxwl == 1: st = ' time'
    else: st = ' times'
    print ('The most frequent symbol(s): ' + ', '.join(maxw) + ' , '
        + str(maxwl) + st)
    if w == 1: st = ' time'
    else: st = ' times'
    print ('The least frequent symbol(s): ' + ', '.join(mins) + ' , '
        + str(w) + st + '\n')

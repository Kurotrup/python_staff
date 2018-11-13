#!/usr/bin/python
'''Decipher an encoded text
Each separate number in the text below is a line number in /etc/dictionaries-common/words (or here). Write a script
which converts the number to a corresponding word. Note that the text contains special characters as well.
 You should leave such characters where they are.
Here is the encoded text:
97419 92425 45424 22860 50690 25188 49846 26422 44857 19374 51598 54896 47302 50629 16484 69869, 90290 46046 22470. 50690 25188 89881 50629, "52079 97825 39434 63729 49700 52242 98947 26422." 65700 32740 90276 55321 56167 90290 27842 92425 45424 40688. 84224 72297 91160 22155 18780 65831 18908 43181 45424, 92425 45424 59720 50690 97004 45838 65907 51435 91160 90290 64424 98103 16484 63751 79139. 33905 50234 50629 59715 65907 91772 22862 90262 90290 64424. 18908 38100 50690 25188 49767 91160 39434 50690 49700? 55376 56167 35694 65901 97444 66123 65004 92425 45424 26422 47079 16484 69869 54896 50690 79139.
NOTE: you are not allowed to use regular expressions in this task.
'''
from os import path
from sys import exit

while True:
    ptf = raw_input('Print a file path for your dictionary where every word placed on new line: ')
    if path.exists(ptf) and path.isfile(ptf):
        break
    elif path.isdir(ptf):
        print 'It`s a directory not a file! Try again\nOr type \'q\' below if you wanna exit'
    elif ptf == 'q' or ptf == 'Q': exit('Goodbye')
    else:
        print 'It`s a wrong path! Try again\nOr type \'q\' below if you wanna exit\n'

n = 0
word_dict = {}
listt = []
encoded_string = '''97419 92425 45424 22860 50690 25188 49846 26422 44857 19374 51598 54896 47302 50629 16484 69869, 90290 46046 22470. 50690 25188 89881 50629, "52079 97825 39434 63729 49700 52242 98947 26422." 65700 32740 90276 55321 56167 90290 27842 92425 45424 40688. 84224 72297 91160 22155 18780 65831 18908 43181 45424, 92425 45424 59720 50690 97004 45838 65907 51435 91160 90290 64424 98103 16484 63751 79139. 33905 50234 50629 59715 65907 91772 22862 90262 90290 64424. 18908 38100 50690 25188 49767 91160 39434 50690 49700? 55376 56167 35694 65901 97444 66123 65004 92425 45424 26422 47079 16484 69869 54896 50690 79139.'''

with open(ptf) as fh:
    for line in fh:
        n += 1
        word_dict[n] = line.strip()

n = ''
for i in encoded_string:
    if i.isdigit():
        n += i
    elif n:
        listt.append(word_dict[int(n)])
        listt.append(i)
        n = ''
    else:
        listt.append(i)

print '\n' + ''.join(listt) + '\n'

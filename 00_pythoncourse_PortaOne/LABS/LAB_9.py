'''Create a program which finds next words inside a body part of an html-document:
1) all words with doubled letters (e.g. "progress", "address", "tool" and so on);
2) all words with articles (e.g. "a computer", "an automatic", "the mentioned", etc.)

The program should search for them outside html-tags, e.g. among words that are "visible" on a screen.
You should point a path to the html-file as an argument to the program. Print all found words to STDOUT.'''
#!/usr/bin/python
import re
from sys import argv
from sys import exit
from os import path

find_body_start = re.compile(r'.*\<body.*')
find_body_end = re.compile(r'.*\<\/body.*')
find_doubl_letrs = re.compile(r'\b((?i)\w*([a-z])\2\w*)\b')
find_shown_text = re.compile(r'<[^<>]+?>')
find_ar = re.compile(r'\b((?i)a|the|any)\s+([a-z]+?)\b')

def print_sp(a,b):
    if a or b:
        for i in xrange(50):
            print '-',
        print ''

usage = 'USAGE: ./LAB_9 <path to file>\n'
flag = len(argv)

if flag < 2:
    exit(usage + 'Need more arguments ')
else:
    ptf = argv[1]
    if path.exists(ptf) and path.isfile(ptf):
        f = open(ptf)
    else: exit('Wrong path to html file')

for line in f:
    find_body = find_body_start.match(line)
    if find_body:
        find_body = ''
        for line in f:
            find_body = find_body_end.match(line)
            line = ''.join(find_shown_text.split(line))
            lettr_much = find_doubl_letrs.findall(line)
            art_much = find_ar.findall(line)
            print_sp(lettr_much,art_much)
            if lettr_much:
                print 'Double lettrs in: ' + ', '.join([''.join(i[0]) for i in lettr_much])
                lettr_much = ''
            if art_much:
                print 'With article: ' + ', '.join([' '.join(i) for i in art_much])
                art_much = ''
            if find_body:
                break
f.close

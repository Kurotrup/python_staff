#!/usr/bin/python
import sys
import os
import re

if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
    HTML_CONTENT = None
    with open(sys.argv[1], 'r') as fh:
        HTML_CONTENT = fh.read()
    print HTML_CONTENT
    raw_input()
    for body in re.findall(">([^<]+)<", HTML_CONTENT):
        words = body.split()
        skip = False
        for i, word in enumerate(words):
            if skip:
                skip = False
                continue
            elif re.match(r"\w*(\w)\1\w*", word):
                print word
            elif re.match("^a$|^an$|^the$", word, re.I):
                print words[i+1]
                skip = True
else:
    sys.exit("Please enter path to file!")

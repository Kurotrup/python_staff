#!/usr/bin/python

import re
import sys
import urllib2

# URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

if len(sys.argv) == 2:
    URL = sys.argv[1]
else:
    print "Point a URL to the html-page as a single argument to the program."
    sys.exit(1)

req = urllib2.Request(URL)
try:
    response = urllib2.urlopen(req)
except urllib2.HTTPError as e:
    print "The server couldn't fulfill the request."
    print "Error code:", e.code
    sys.exit(2)
except urllib2.URLError as e:
    print "We failed to reach a server."
    print "Reason:", e.reason
    sys.exit(3)

html = response.read()

html_body_start = html.find("<body")
html_body_end = html.rfind("</body>") + 7
html_body = html[html_body_start:html_body_end]

cut_tags = ['script', 'style', 'form']
cut_tags_pat = '|'.join(['(?:<{0:s}>.*</{0:s}>)'.format(tag) for tag in cut_tags])
print cut_tags_pat

html_body_raw = re.sub(cut_tags_pat, '', html_body)
html_body_text = re.sub(r'<[^>]+>', '', html_body_raw)

pat1 = r'\b([a-z]*([a-z])\2+[a-z]*)\b'
regex1 = re.compile(pat1, re.I)
res1 = [m[0] for m in regex1.findall(html_body_text)]
print "Words with doubled letters:"
print set(res1)
print ""

articles = ['a', 'an', 'the']
pat2 = r'\b(%s)\s([a-z]+)\b' % '|'.join(articles)
regex2 = re.compile(pat2, re.I)
res2 = [' '.join(m) for m in regex2.findall(html_body_text)]
print "Words with articles:"
print set(res2)

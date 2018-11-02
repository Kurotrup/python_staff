''' A task is the same as the previous one, but this time you need to create
an iterator, which returns random vertex coordinates.
Your program should be universal and
support 1D, 2D, 3D, ... ND spaces. A desired number of dimensions
 may be supplied by a user as an optional program argument.
Use generators while working on the task.'''
import random
import math
from sys import argv
def generator_f(n):
    while True:
        rez = [random.uniform(-100,100) for i in xrange(n)]
        yield rez

# def rast(m):
#     a = 0
#     for i in m:
#         a += i**2
#     return math.sqrt(a)

flag = len(argv)
n = 3
if flag > 1 and argv[1].isdigit():
    n = int(argv[1])

it = generator_f(n)
#l = sorted([it.next() for c in xrange(random.randint(0,100))], key = rast)
l = sorted([it.next() for c in xrange(random.randint(0,100))], key = lambda x: math.sqrt(sum([i**2 for i in x])))
for c in l:
    for i in c:
        print format(i,'6.2f').rjust(8) + " ",
    print ''

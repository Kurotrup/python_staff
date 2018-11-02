#!/usr/bin/python

import sys
from math import sqrt
from random import randint, uniform

MAX_COORD = 1000
MAX_POINTS = 100

# http://docs.quantifiedcode.com/python-anti-patterns/correctness/assigning_a_lambda_to_a_variable.html
# rand_coord = lambda : uniform(-MAX_COORD, MAX_COORD)
# dist = lambda p: sqrt(sum([c**2 for c in p]))

def rand_coord(): return uniform(-MAX_COORD, MAX_COORD)

def dist(p): return sqrt(sum([c**2 for c in p]))

def points_arr_pretty_print(points_arr, verbose=False):
    for point in points_arr:
        for coord in point:
            print "{0: > 8.2f} ".format(coord),
        if verbose:
            print " "*3 + "dist={0:<.2f}".format(dist(point)),
        print ""


points_number = randint(1, MAX_POINTS)

points_arr = [[rand_coord() for c in xrange(3)] for n in xrange(points_number)]
points_arr.sort(key=dist)

print "Number of points: {0:d}".format(points_number)
print "Points coordinates sorted by the point distance to the coordinate center:"
points_arr_pretty_print(points_arr, sys.argv[-1]=='-v')

#
# additional task
#
# points_total_dist_arr = [
#     sum([sqrt(sum([(pn[c] - p[c])**2 for c in range(3)])) for pn in points_arr])
#     for p in points_arr
# ]
# points_arr_sorted = [x[1] for x in sorted(zip(points_total_dist_arr, points_arr))]
#
# print "Points coordinates sorted by the total point distance to other points:"
# points_arr_pretty_print(points_arr_sorted)

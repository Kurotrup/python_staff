import sys
from math import sqrt
from random import randint, uniform

MAX_COORD = 1000
MAX_POINTS = 100

def dist(p): return sqrt(sum([c**2 for c in p]))

def rand_points_arr_generator(dimensions):
    points_number = randint(1, MAX_POINTS)
    while points_number:
        points_number -= 1
        yield tuple(uniform(-MAX_COORD, MAX_COORD) for c in xrange(dimensions))

def points_arr_pretty_print(points_arr, verbose=False):
    for point in points_arr:
        for coord in point:
            print "{0: > 8.2f} ".format(coord),
        if verbose:
            print " "*3 + "dist={0:<.2f}".format(dist(point)),
        print ""


dimensions = 3

args_is_ok = True
if len(sys.argv) >=2:
    try:
        dimensions = int(sys.argv[1])
    except ValueError:
        args_is_ok = False
    else:
        if dimensions <= 0:
            args_is_ok = False
if not args_is_ok:
    print('Please, check specified arguments')
    print('Usage: %s [dimensions [-v]]' % sys.argv[0])
    sys.exit(1)


points_arr = list(rand_points_arr_generator(dimensions))
points_arr.sort(key=dist)

print "Number of points: {0:d}".format(len(points_arr))
print "Points coordinates sorted by the point distance to the coordinate center:"
points_arr_pretty_print(points_arr, sys.argv[-1]=='-v')

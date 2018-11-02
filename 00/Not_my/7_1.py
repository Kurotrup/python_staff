#!/usr/bin/env python
import sys
import random
import math
def point_generator():
    """Returns random point in n-dimensional space"""
    point = []
    for x in range(dimensions):
        point.append(round(random.uniform(-100,100), 2))
    yield tuple(point)

def get_distance(p1, p2):
    """Returns distance between two points in n-dimensional space.
    Points must be presented as n-lenght number tuples."""
    diffs = ((p2[x] - p1[x])**2 for x in range(dimensions))
    return math.sqrt(sum(diffs))

def adjust(point):
    """Forces fields to be right-aligned"""
    pattern = ""
    for x in range(dimensions):
        pattern = pattern + "{:>12}"
    return pattern.format(*point)

dimensions = 3

if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        dimensions = int(sys.argv[1])
    else:
        sys.exit("Wrong number of dimensions: " + sys.argv[1])

length = random.randint(0, 100)
points = (next(point_generator()) for x in range(length))

pointdict = {}
zero = tuple([0 for x in range(dimensions)])
for x in range(length):
    point = next(points)
    pointdict[get_distance(zero, point)] = point

for distance in sorted(pointdict):
    print adjust(pointdict[distance])

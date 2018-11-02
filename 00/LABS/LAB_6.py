'''Create a list of random points in 3 dimensional space
 (each point is described by 3 float coordinates).
Coordinates values may be negative as well. A size of the list
 should also be random.Sort the points by their distance to the coordinate center.
Print a resulted list as a table, where each column represents a corresponding point coordinate. Format the output to have all numbers justified to the right side:
  0.57  -22.21   19.28
 -6.35   24.86  -49.71
-20.45  -82.54   25.89
-29.36    6.75  -86.36
-25.67   29.72   97.17
-53.01  -76.89   48.80
-73.47    0.01   77.37
-11.18  -99.66  -54.90
  3.72   83.11   92.97
-84.94  -83.79  -82.65 '''
import random
import math
l= [[random.uniform(-100,100),random.uniform(-100,100),random.uniform(-100,100)] for c in xrange(random.randint(0,100))]
l = sorted(l, key = lambda x: math.sqrt(x[0]**2 + x[1]**2 + x[2]**2))
for c in l:
    print format(c[0],'6.2f').rjust(8) + " " + format(c[1],'6.2f').rjust(8) + ' ' + format(c[2],'6.2f').rjust(8)

#!/usr/bin/env python
# ============================================================================
import sys
import math

# ===========================================================================
# = http://projecteuler.net/problem=39                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = if p is the perimeter of right triangle wtih integral length sides,     =
# = find which p <= 1000 maximizes the number of solutions {a,b,c}          =
# ===========================================================================

# -----------------------------------------------------------------------------
def findNumTriangles(p):
    num_triangles = 0
    for c in xrange(p):
        for a in xrange(1, c):
            b = p - c - a
            if a > b or b < 1:
                continue
            # if a**2 + b**2 == c**2:
            if a*a + b*b == c*c:
                num_triangles += 1
    return num_triangles

# -----------------------------------------------------------------------------
def findMaxTriangles(max_perimeter):
    # num_triangles = [0]*(max_perimeter+1)
    max_triangles = 0
    max_p = 0

    for p in xrange(max_perimeter+1):
        if p%2 == 1:
            continue
        num_triangles = findNumTriangles(p)
        if num_triangles > max_triangles:
            max_triangles = num_triangles
            max_p = p
        # num_triangles[p] = findNumTriangles(p)

    print 'The maximun number of solutions occurs at p: %d - %d solution' \
            % (max_p, max_triangles)
    return max_p


# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  print findNumTriangles(120)
  print findMaxTriangles(1000)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# The maximun number of solutions occurs at p: 840 - 8 solution

#!/usr/bin/env python
# ============================================================================
import sys
import math

# ===========================================================================
# = http://projecteuler.net/problem=53                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Find the number of values for (n choose r) which exceed 1e6 where       =
# = 1 <= n <= 100                                                           =
# ===========================================================================

# ------------------------------------------------------------------------------
def nChooseR(n, r):
    return math.factorial(n) / ( math.factorial(r)*math.factorial(n-r) )

# ------------------------------------------------------------------------------
def findFirstCombination(n, thresh = 1e6):
    max_scan = n/2 + n%2
    print 'for n = %s, scanning to: %s' % (n, max_scan)
    for i in xrange(max_scan):
        if nChooseR(n, i) > thresh:
            return i
    return None

# ------------------------------------------------------------------------------
def findNumCombinationsAboveThreshold(x_min, x_max, thresh = 1e6):
    num_above_threshold = 0
    for x in xrange(x_min, x_max+1):
        first_above_threshold = findFirstCombination(x, thresh)
        print 'x: %d - first_above_threshold: %s' % (x, first_above_threshold)
        if first_above_threshold is not None:
            num_above_threshold += x-2*first_above_threshold + 1
    return num_above_threshold

# ============================================================================
def main():
    print 'num combinations above 1e6: %d' % findNumCombinationsAboveThreshold(1, 100)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# num combinations above 1e6: 4075
#
# real	0m0.101s
# user	0m0.025s
# sys	0m0.036s

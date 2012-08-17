#!/usr/bin/env python
# ============================================================================
import sys
import math

# ===========================================================================
# = http://projecteuler.net/problem=38                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# =                                                                         =
# =                                                                         =
# ===========================================================================

# -----------------------------------------------------------------------------
def isPandigital(cand):
    sorted_string = ''.join(sorted('%d' % cand))
    return sorted_string == '123456789'

# -----------------------------------------------------------------------------
def getProductSum(cand):
    sum = cand*1e5 + 2*cand
    return sum

# -----------------------------------------------------------------------------
def findMaxPandigitalSum():
    max = 918273645
    for i in xrange(9123, 9877):
        product_sum = getProductSum(i)
        if not isPandigital(product_sum): continue
        if product_sum > max:
            max = product_sum
    print 'The max product sum is %d' % max
    return max

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  findMaxPandigitalSum()


# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# The max product sum is 932718654
#!/usr/bin/env python
# =============================================================================
import sys
import math
import operator

import primes_pp

# =============================================================================
# = http://projecteuler.net/problem=43                                        =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Some 0-9 pandigitals have the following property:                         =
# =   Consider the number: 1406357289                                         =
# =   Let d1 be the 1st digit, d2 be the 2nd digit, and so on.                =
# =   In this way, we note the following:                                     =
# =                                                                           =
# =   d2d3d4=406 is divisible by 2                                            =
# =   d3d4d5=063 is divisible by 3                                            =
# =   d4d5d6=635 is divisible by 5                                            =
# =   d5d6d7=357 is divisible by 7                                            =
# =   d6d7d8=572 is divisible by 11                                           =
# =   d7d8d9=728 is divisible by 13                                           =
# =   d8d9d10=289 is divisible by 17                                          =
# = We want to find all such numbers                                          =
# =============================================================================

# -----------------------------------------------------------------------------
def genMultiplesList(mult):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    start = 012
    while not (start % mult) == 0:
        start += 1

    list = []
    for l in xrange(start, 988, mult):
        if (len(set('%03d' % l)) == 3):
            list.append('%03d' % l)

    return list

# -----------------------------------------------------------------------------
def findSpecialPandigitals():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    dicts = []
    dicts.append(genMultiplesList(2))
    dicts.append(genMultiplesList(3))
    dicts.append(genMultiplesList(5))
    dicts.append(genMultiplesList(7))
    dicts.append(genMultiplesList(11))
    dicts.append(genMultiplesList(13))
    dicts.append(genMultiplesList(17))

    for d in dicts:
        print '----------------------'
        print d

# =============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  findSpecialPandigitals()

# =============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# =============================================================================
# ============
# = solution =
# ============

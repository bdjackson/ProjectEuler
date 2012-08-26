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
def flatten(l, level = 0):
    """
    takes a list of lists, and flattens into a single list
    """
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    flat_l = []
    if isinstance(l, list):
        for e in l:
            flat_l += flatten(e)
    else:
        flat_l = [l]

    return flat_l

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
def constructSpecialNumbers(dicts, seed = ''):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    if len(dicts) == 0: return seed

    special_nums = []
    for d in dicts[0]:
        if seed == '':
            special_nums.append( constructSpecialNumbers( dicts[1:]
                                                        , d
                                                        )
                               )
        if seed[-2:] == d[:2]:
            special_nums.append( constructSpecialNumbers( dicts[1:]
                                                        , '%s%s' % (seed, d[-1])
                                                        )
                               )

    return flatten(special_nums)

# -----------------------------------------------------------------------------
def pruneNonPandigitals(special_nums):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    special_pandigitals = []
    ref = set('0123456789')
    for sn in special_nums:
        if set(sn) == ref:
            special_pandigitals.append(int(sn))
    return special_pandigitals

# -----------------------------------------------------------------------------
def findSpecialPandigitals():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    dicts = []
    dicts.append(genMultiplesList(1))
    dicts.append(genMultiplesList(2))
    dicts.append(genMultiplesList(3))
    dicts.append(genMultiplesList(5))
    dicts.append(genMultiplesList(7))
    dicts.append(genMultiplesList(11))
    dicts.append(genMultiplesList(13))
    dicts.append(genMultiplesList(17))

    special_nums = constructSpecialNumbers(dicts)
    special_pandigitals = pruneNonPandigitals(special_nums)
    print 'The list of special pandigitals is:'
    print '\t%s' % special_pandigitals
    print 'The sum of these numbers is: %d' % reduce( operator.add
                                                    , special_pandigitals
                                                    )

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
# The list of special pandigitals is:
# 	[1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]
# The sum of these numbers is: 16695334890
#
# real	0m1.701s
# user	0m1.679s
# sys	0m0.019s


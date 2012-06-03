#!/usr/bin/env python 
# ============================================================================
import sys
import math

# ===========================================================================
# = http://projecteuler.net/problem=44                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Find the pair of pentagonal numbers whos sum and difference are both    =
# = pentagonal.  If there are multiple such numbers, find the pair with the =
# = smallest difference                                                     =
# ===========================================================================

# -----------------------------------------------------------------------------
def isPentagonalNumber(num):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  return ( (1 + math.sqrt(1+4*3*2*num))%6 == 0 )

# -----------------------------------------------------------------------------
def nextPentagonalNumber(i):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  return (3*i-2)

# -----------------------------------------------------------------------------
def findPentagonalPair():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  i = 0
  pa = 0
  diff = -1

  while diff < 0:
    i += 1
    pa += nextPentagonalNumber(i)
    
    j = 1
    pd = 1
    while pd < pa:

      nb = pa-pd
      if isPentagonalNumber(nb):
        nc = pa+nb
        if (isPentagonalNumber(nc)):
          diff = pa-nb
      j += 1
      pd += nextPentagonalNumber(j)
    assert(i<1e7)
  print 'The pair of pentagonal numbers is (%d, %d), with a difference of %d' % (pa, (pa-diff), diff)

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findPentagonalPair()
  print '====================================================================='
  print 'i: %d - %s' % (7042750          , isPentagonalNumber(7042750          ))
  print 'i: %d - %s' % (1560090          , isPentagonalNumber(1560090          ))
  print 'i: %d - %s' % (7042750 - 1560090, isPentagonalNumber(7042750 - 1560090))
  print 'i: %d - %s' % (7042750 + 1560090, isPentagonalNumber(7042750 + 1560090))
  print '====================================================================='

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# 5482660

# ( 7042750
# , 1560090
# ) 5482660
# 
